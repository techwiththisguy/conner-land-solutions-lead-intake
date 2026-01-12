from flask import Blueprint, render_template, request, redirect, url_for, flash

public_bp = Blueprint("public", __name__)

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
        
        if not name or not phone or not service_type or not location or not notes:
            flash("Please fill out all required fields.", "error")
            return render_template("request_quote.html")
        
        flash("Quote request received! We'll contact you shortly." "success")
        return redirect(url_for("public.request_quote"))
    
    return render_template("request_quote.html")