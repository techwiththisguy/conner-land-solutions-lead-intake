from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import db, Lead
from flask import current_app

public_bp = Blueprint("public", __name__)

def require_admin():
    if not session.get("is_admin"):
        return redirect(url_for("public.admin_login"))
    return None

@public_bp.get("/")
def index():
    return render_template("index.html")

@public_bp.route("/request-quote", methods=["GET", "POST"])
def request_quote():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        service_type = request.form.get("service_type", "").strip()
        location = request.form.get("location", "").strip()
        notes = request.form.get("notes", "").strip()
        
        # Validation
        if not name or not phone or not service_type or not location or not notes:
            flash("Please fill out all required fields.", "error")
            return render_template("request_quote.html")
        
        lead = Lead(
            name=name,
            phone=phone,
            email=request.form.get("email", "").strip() or None,
            service_type=service_type,
            location=location,
            address=request.form.get("address", "").strip() or None,
            notes=notes,
        )
        
        db.session.add(lead)
        db.session.commit()
        
        # Success Message
        flash("Quote request received! We'll contact you shortly.")
        return redirect(url_for("public.request_quote"))
    
    # Get Request
    return render_template("request_quote.html")

@public_bp.get("/admin/leads")
def admin_leads():
    guard = require_admin()
    if guard:
        return guard
    
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return render_template("admin_leads.html", leads=leads)

@public_bp.post("/admin/leads/<int:lead_id>/status")
def update_lead_status(lead_id):
    guard = require_admin()
    if guard:
        return guard
        
    lead = Lead.query.get_or_404(lead_id)
    new_status = request.form.get("status", "").strip()
    
@public_bp.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == current_app.config.get("ADMIN_PASSWORD"):
            session["is_admin"] = True
            flash("Logged in.", "success")
            return redirect(url_for("public.admin_leads"))
        
        flash("Incorrect password.", "error")
        return redirect(url_for("public.admin_login"))
    
    return render_template("admin_login.html")

@public_bp.get("/admin/logout")
def admin_logout():
    session.pop("is_admin", None)
    flash("Logged out.", "success")
    return redirect(url_for("public.index"))
    
    allowed = {"NEW", "CONTACTED", "CLOSED", "LOST"}
    if new_status not in allowed:
        flash("Invalid status.", "error")
        return redirect(url_for("public.admin_leads"))
    
    lead.status = new_status
    db.session.commit()
    
    flash("Lead status updated.", "success")
    return redirect(url_for("public.admin_leads"))