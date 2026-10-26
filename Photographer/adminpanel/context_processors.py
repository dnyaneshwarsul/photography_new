from .models import AdminProfile

def admin_context(request):
    admin_id = request.session.get("admin_id")
    admin_name = request.session.get("admin_name")
    admin_email = request.session.get("admin_email")
    admin_obj = None

    if admin_id:
        admin_obj = AdminProfile.objects.filter(id=admin_id).first()
    
    if not admin_obj and admin_email:
        admin_obj = AdminProfile.objects.filter(admin_email__iexact=admin_email).first()

    if not admin_obj:
        admin_obj = AdminProfile.objects.first()

    if admin_obj:
        display_name = admin_obj.admin_name
        email = admin_obj.admin_email
        profile_img = admin_obj.admin_profile.url if admin_obj.admin_profile else None
    else:
        display_name = admin_name or "Dnyaneshwar Sul"
        email = admin_email or "dnyaneshwarsul61@gmail.com"
        profile_img = None

    return {
        'logged_admin': admin_obj,
        'admin_display_name': display_name,
        'admin_display_email': email,
        'admin_profile_img': profile_img,
    }
