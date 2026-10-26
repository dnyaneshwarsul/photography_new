from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
import datetime
from .models import Booking, ContactInquiry
from adminpanel.models import HomeSlider, HomeAbout, AboutPageInfo, HomeService, HomeFeaturedWork, HomeCategory, HomeVideoStory, HomeGallery, HomeWhyUs, HomeWhyUsHeader, HomeProcess, HomeProcessHeader, HomeClientStory, HomeTestimonial, HomeInstaPost, HomeAward, AboutStory, ServicesHero, HomeWhatWeOfferHeader, HomeWhatWeOfferItem, CategoryHero, ServicesCTA, CategorySectionHeader, GalleryHero, GallerySectionHeader, GalleryCTA, ContactHero, ContactInfo

# ── HOME PAGE ──
def index(req):
    sliders = HomeSlider.objects.all().order_by("id")
    about_data = HomeAbout.objects.last()
    services_list = HomeService.objects.all().order_by("id")
    featured_works = HomeFeaturedWork.objects.all().order_by("id")
    categories_list = HomeCategory.objects.all().order_by("id")
    video_stories = HomeVideoStory.objects.all().order_by("id")
    recent_galleries = HomeGallery.objects.all().order_by("id")
    why_us_items = HomeWhyUs.objects.all().order_by("id")
    process_steps = HomeProcess.objects.all().order_by("id")
    client_stories = HomeClientStory.objects.all().order_by("id")
    testimonials = HomeTestimonial.objects.all().order_by("id")
    insta_posts = HomeInstaPost.objects.all().order_by("id")
    awards = HomeAward.objects.all().order_by("id")

    # What We Offer Section Data
    offer_header = HomeWhatWeOfferHeader.objects.last()
    if not offer_header:
        offer_header = HomeWhatWeOfferHeader.objects.create(
            small_title="WHAT WE OFFER",
            title="More Than Just Photography",
            description="We provide complete photography solutions to make your special moments beautiful, memorable and timeless."
        )

    if not HomeWhatWeOfferItem.objects.exists():
        default_items = [
            {
                "icon_class": "bi bi-camera",
                "title": "Professional Photography",
                "description": "High-quality photography using professional equipment and creative techniques."
            },
            {
                "icon_class": "bi bi-camera-reels",
                "title": "Cinematic Videography",
                "description": "Beautiful cinematic videos that bring your most memorable moments back to life."
            },
            {
                "icon_class": "bi bi-image",
                "title": "Professional Editing",
                "description": "Carefully edited photographs with professional color correction and finishing."
            },
            {
                "icon_class": "bi bi-cloud-arrow-down",
                "title": "Digital Delivery",
                "description": "Receive your beautiful photographs through a convenient online digital gallery."
            }
        ]
        for item in default_items:
            HomeWhatWeOfferItem.objects.create(**item)

    offer_items = HomeWhatWeOfferItem.objects.all().order_by("id")

    # How We Work Section Data
    process_header = HomeProcessHeader.objects.last()
    if not process_header:
        process_header = HomeProcessHeader.objects.create(
            small_title="OUR PROCESS",
            title="How We Work",
            description="From the first conversation to the final delivery, we make your photography experience simple and enjoyable."
        )

    if not HomeProcess.objects.exists():
        default_process_steps = [
            {
                "step_number": "01",
                "icon_class": "bi bi-chat-heart",
                "title": "Consultation",
                "description": "Understand your requirements and photography ideas."
            },
            {
                "step_number": "02",
                "icon_class": "bi bi-calendar-check",
                "title": "Planning",
                "description": "Plan locations, concepts, outfits and schedule."
            },
            {
                "step_number": "03",
                "icon_class": "bi bi-camera",
                "title": "Photoshoot",
                "description": "Capture natural emotions and beautiful moments."
            },
            {
                "step_number": "04",
                "icon_class": "bi bi-check-circle",
                "title": "Delivery",
                "description": "Professionally edited images delivered to you."
            }
        ]
        for step in default_process_steps:
            HomeProcess.objects.create(**step)

    process_steps = HomeProcess.objects.all().order_by("step_number")

    return render(req, "website/index.html", {
        "active_page": "home",
        "sliders": sliders,
        "about_data": about_data,
        "services": services_list,
        "featured_works": featured_works,
        "categories": categories_list,
        "video_stories": video_stories,
        "recent_galleries": recent_galleries,
        "why_us_items": why_us_items,
        "process_steps": process_steps,
        "process_header": process_header,
        "client_stories": client_stories,
        "testimonials": testimonials,
        "insta_posts": insta_posts,
        "awards": awards,
        "offer_header": offer_header,
        "offer_items": offer_items
    })


# ── ABOUT PAGE ──
def about(req):
    hero_data = AboutPageInfo.objects.filter(hero_title__isnull=False).exclude(hero_title='').last()
    about_data = AboutPageInfo.objects.filter(id=1).first() or AboutPageInfo.objects.last()
    numbers_info = AboutPageInfo.objects.last()
    if not numbers_info:
        numbers_info = AboutPageInfo.objects.create()
    
    home_about = HomeAbout.objects.last()
    if not about_data:
        about_data = home_about or numbers_info

    if about_data:
        for field in ['numbers_small_title', 'numbers_title', 'numbers_desc',
                      'stat1_count', 'stat1_title', 'stat1_icon',
                      'stat2_count', 'stat2_title', 'stat2_icon',
                      'stat3_count', 'stat3_title', 'stat3_icon',
                      'stat4_count', 'stat4_title', 'stat4_icon',
                      'cta_small_title', 'cta_title', 'cta_desc',
                      'cta_btn1_text', 'cta_btn1_link', 'cta_btn2_text', 'cta_btn2_link', 'cta_bg_image']:
            if not getattr(about_data, field, None) and hasattr(numbers_info, field):
                setattr(about_data, field, getattr(numbers_info, field))

    if home_about and about_data != home_about:
        if not getattr(about_data, 'about_image', None) and home_about.about_image:
            about_data.about_image = home_about.about_image
        if not getattr(about_data, 'small_title', None):
            about_data.small_title = home_about.small_title
        if not getattr(about_data, 'title', None):
            about_data.title = home_about.title
        if not getattr(about_data, 'description_para1', None):
            about_data.description_para1 = home_about.description_para1
        if not getattr(about_data, 'description_para2', None):
            about_data.description_para2 = home_about.description_para2
        if hasattr(home_about, 'experience_years') and home_about.experience_years and not getattr(about_data, 'experience_years', None):
            about_data.experience_years = home_about.experience_years
            about_data.experience_text = home_about.experience_text
            about_data.feature1_title = home_about.feature1_title
            about_data.feature1_desc = home_about.feature1_desc
            about_data.feature1_icon = home_about.feature1_icon
            about_data.feature2_title = home_about.feature2_title
            about_data.feature2_desc = home_about.feature2_desc
            about_data.feature2_icon = home_about.feature2_icon
            about_data.feature3_title = home_about.feature3_title
            about_data.feature3_desc = home_about.feature3_desc
            about_data.feature3_icon = home_about.feature3_icon

    why_us_items = HomeWhyUs.objects.all().order_by("id")
    testimonials = HomeTestimonial.objects.all().order_by("id")
    awards = HomeAward.objects.all().order_by("id")
    services_list = HomeService.objects.all().order_by("id")
    client_stories = HomeClientStory.objects.all().order_by("id")
    process_steps = HomeProcess.objects.all().order_by("id")
    our_story_steps = AboutStory.objects.all().order_by("id")
    our_story_data = AboutStory.objects.last()
    
    return render(req, "website/about.html", {
        "active_page": "about",
        "hero_data": hero_data,
        "about_data": about_data,
        "our_story_data": our_story_data,
        "why_us_items": why_us_items,
        "testimonials": testimonials,
        "awards": awards,
        "services": services_list,
        "client_stories": client_stories,
        "process_steps": process_steps,
        "our_story_steps": our_story_steps
    })

def services(req):
    services_list = HomeService.objects.all().order_by("id")
    process_steps = HomeProcess.objects.all().order_by("id")
    why_us_items = HomeWhyUs.objects.all().order_by("id")
    featured_works = HomeFeaturedWork.objects.all().order_by("id")
    recent_galleries = HomeGallery.objects.all().order_by("id")
    about_data = AboutPageInfo.objects.last()
    service_hero = ServicesHero.objects.last()
    
    offer_header = HomeWhatWeOfferHeader.objects.last()
    if not offer_header:
        offer_header = HomeWhatWeOfferHeader.objects.create(
            small_title="WHAT WE OFFER",
            title="More Than Just Photography",
            description="We provide complete photography solutions to make your special moments beautiful, memorable and timeless."
        )

    if not HomeWhatWeOfferItem.objects.exists():
        default_items = [
            {
                "icon_class": "bi bi-camera",
                "title": "Professional Photography",
                "description": "High-quality photography using professional equipment and creative techniques."
            },
            {
                "icon_class": "bi bi-camera-reels",
                "title": "Cinematic Videography",
                "description": "Beautiful cinematic videos that bring your most memorable moments back to life."
            },
            {
                "icon_class": "bi bi-image",
                "title": "Professional Editing",
                "description": "Carefully edited photographs with professional color correction and finishing."
            },
            {
                "icon_class": "bi bi-cloud-arrow-down",
                "title": "Digital Delivery",
                "description": "Receive your beautiful photographs through a convenient online digital gallery."
            }
        ]
        for item in default_items:
            HomeWhatWeOfferItem.objects.create(**item)

    offer_items = HomeWhatWeOfferItem.objects.all().order_by("id")

    process_header = HomeProcessHeader.objects.last()
    if not process_header:
        process_header = HomeProcessHeader.objects.create(
            small_title="OUR PROCESS",
            title="How We Work",
            description="From the first conversation to the final delivery, we make your photography experience simple and enjoyable."
        )

    if not HomeProcess.objects.exists():
        default_process_steps = [
            {
                "step_number": "01",
                "icon_class": "bi bi-chat-heart",
                "title": "Consultation",
                "description": "Understand your requirements and photography ideas."
            },
            {
                "step_number": "02",
                "icon_class": "bi bi-calendar-check",
                "title": "Planning",
                "description": "Plan locations, concepts, outfits and schedule."
            },
            {
                "step_number": "03",
                "icon_class": "bi bi-camera",
                "title": "Photoshoot",
                "description": "Capture natural emotions and beautiful moments."
            },
            {
                "step_number": "04",
                "icon_class": "bi bi-check-circle",
                "title": "Delivery",
                "description": "Professionally edited images delivered to you."
            }
        ]
        for step in default_process_steps:
            HomeProcess.objects.create(**step)

    process_steps = HomeProcess.objects.all().order_by("step_number")
    
    why_us_header = HomeWhyUsHeader.objects.last()
    if not why_us_header:
        why_us_header = HomeWhyUsHeader.objects.create(
            small_title="ABOUT ME",
            title="Turning Beautiful Moments Into Timeless Memories",
            description="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
        )

    if not HomeWhyUs.objects.exists():
        default_why_us = [
            {
                "icon_class": "bi bi-camera",
                "title": "Professional",
                "description": "Professional photography with creative ideas."
            },
            {
                "icon_class": "bi bi-lightning",
                "title": "Creative",
                "description": "Unique concepts and creative photography."
            },
            {
                "icon_class": "bi bi-heart",
                "title": "Passionate",
                "description": "We capture every moment with passion."
            },
            {
                "icon_class": "bi bi-award",
                "title": "Quality",
                "description": "High-quality images and professional editing."
            }
        ]
        for item in default_why_us:
            HomeWhyUs.objects.create(**item)

    services_cta = ServicesCTA.objects.last()
    if not services_cta:
        services_cta = ServicesCTA.objects.create()

    return render(req, "website/services.html", {
        "active_page": "services",
        "services": services_list,
        "process_steps": process_steps,
        "process_header": process_header,
        "why_us_header": why_us_header,
        "why_us_items": why_us_items,
        "featured_works": featured_works,
        "recent_galleries": recent_galleries,
        "about_data": about_data,
        "service_hero": service_hero,
        "offer_header": offer_header,
        "offer_items": offer_items,
        "services_cta": services_cta
    })

def category(req):
    if not HomeCategory.objects.exists():
        default_cats = [
            {
                "category_name": "Wedding Photography",
                "description": "Capture every beautiful emotion, sacred ritual, and unforgettable celebration of your special wedding day.",
                "sub_services": "Candid Wedding Photography\nTraditional Ceremony Coverage\nBridal & Groom Solo Portraits\nCinematic Highlight Reel & Teaser"
            },
            {
                "category_name": "Pre-Wedding Photography",
                "description": "Tell your romantic love story before the wedding with stunning outdoor and conceptual couple photoshoots.",
                "sub_services": "Scenic Outdoor Location Shoots\nTheme & Concept Shoot\nDrone Aerial Couple Shots\nReel & Short Promo Videos"
            },
            {
                "category_name": "Portrait Photography",
                "description": "Expressive solo, lifestyle, and professional portrait photography highlighting natural beauty and personality.",
                "sub_services": "Studio Lighting Setup\nOutdoor Lifestyle Portraits\nProfessional Headshots\nCreative Concept Styling"
            },
            {
                "category_name": "Event & Party Photography",
                "description": "Vibrant photography coverage for birthdays, anniversaries, corporate functions, and family gatherings.",
                "sub_services": "Full Event Coverage\nGuest & Group Moments\nStage & Performance Shots\nQuick Digital Album Delivery"
            },
            {
                "category_name": "Maternity & Baby Shoot",
                "description": "Gentle, heartwarming maternity, newborn, and baby milestone photography captured with love and care.",
                "sub_services": "Maternity Bump Shoot\nNewborn Cozy Props Setup\n1st Birthday Cake Smash\nFamily Milestone Portraits"
            }
        ]
        for c in default_cats:
            HomeCategory.objects.create(**c)

    categories_list = HomeCategory.objects.all().order_by("id")
    category_hero = CategoryHero.objects.last()
    if not category_hero:
        category_hero = CategoryHero.objects.create(
            label_text="Photography Categories",
            title_prefix="Explore Our ",
            title_highlight="Photography",
            title_suffix=" Categories",
            description="Discover professional photography services for every special moment, occasion and beautiful story you want to preserve forever.",
            btn_text="Explore Categories",
            btn_link="#all-categories"
        )
    about_data = AboutPageInfo.objects.last()
    services_cta = ServicesCTA.objects.last()
    video_stories = HomeVideoStory.objects.all().order_by("id")
    category_section_header = CategorySectionHeader.objects.last()
    if not category_section_header:
        category_section_header = CategorySectionHeader.objects.create()

    return render(req, "website/category.html", {
        "active_page": "category",
        "categories": categories_list,
        "category_hero": category_hero,
        "about_data": about_data,
        "services_cta": services_cta,
        "video_stories": video_stories,
        "category_section_header": category_section_header
    })


def photography(req):
    return render(req, "website/photography.html", {"active_page": "photography"})


def gallery(req):
    gallery_hero = GalleryHero.objects.last()
    if not gallery_hero:
        gallery_hero = GalleryHero.objects.create(
            small_title="OUR PHOTOGRAPHY COLLECTION",
            title="Photo Gallery",
            description="Explore our collection of beautiful photographs, capturing love, happiness, celebrations and unforgettable moments that deserve to be remembered forever."
        )

    # Fetch section headers
    headers = {h.section_key: h for h in GallerySectionHeader.objects.all()}
    
    wedding_header = headers.get("wedding") or GallerySectionHeader(small_title="Love & Forever", title="Wedding Photography", description="Beautiful wedding moments captured with emotions, traditions, happiness and timeless memories.")
    prewedding_header = headers.get("prewedding") or GallerySectionHeader(small_title="Couple Stories", title="Pre-Wedding Photography", description="Romantic couple sessions filled with love, beautiful locations and natural emotions.")
    birthday_header = headers.get("birthday") or GallerySectionHeader(small_title="Celebration", title="Birthday Photography", description="Joyful birthday celebrations, party moments, cake cutting and happy memories.")
    baby_header = headers.get("baby") or GallerySectionHeader(small_title="Little Memories", title="Baby & Kids Photography", description="Adorable baby portraits, maternity shoots and heartwarming childhood smiles.")
    events_header = headers.get("events") or GallerySectionHeader(small_title="Special Events", title="Event Photography", description="Corporate events, parties, family gatherings and special occasions captured with precision.")
    fashion_header = headers.get("fashion") or GallerySectionHeader(small_title="Style & Creativity", title="Fashion Photography", description="Creative model portfolios, fashion shoots, stylish outfits and artistic portraits.")
    portrait_header = headers.get("portrait") or GallerySectionHeader(small_title="Personal Stories", title="Portrait Photography", description="Expressive solo portraits, headshots and personal photography sessions.")

    # Fetch gallery items categorized for each section
    wedding_items = list(HomeGallery.objects.filter(category_name__iexact="Wedding").order_by("-id"))
    prewedding_items = list(HomeGallery.objects.filter(category_name__iexact="Pre-Wedding").order_by("-id"))
    birthday_items = list(HomeGallery.objects.filter(category_name__iexact="Birthday").order_by("-id"))
    baby_items = list(HomeGallery.objects.filter(category_name__iexact="Baby & Kids").order_by("-id"))
    events_items = list(HomeGallery.objects.filter(category_name__iexact="Events").order_by("-id"))
    fashion_items = list(HomeGallery.objects.filter(category_name__iexact="Fashion").order_by("-id"))
    portrait_items = list(HomeGallery.objects.filter(category_name__iexact="Portrait").order_by("-id"))

    # Also get unassigned gallery items if any
    uncategorized = list(HomeGallery.objects.exclude(category_name__in=["Wedding", "Pre-Wedding", "Birthday", "Baby & Kids", "Events", "Fashion", "Portrait"]).order_by("-id"))
    if uncategorized and not wedding_items:
        wedding_items = uncategorized

    # Fetch Gallery CTA Banner Data
    gallery_cta = GalleryCTA.objects.last()
    if not gallery_cta:
        gallery_cta = GalleryCTA.objects.create(
            title="Have a Moment to Capture?",
            description="Let's turn your special moments into beautiful memories that you can cherish forever.",
            btn1_text="Book a Photoshoot",
            btn1_link="/booking_form/",
            btn2_text="Contact Us",
            btn2_link="/contact/"
        )

    return render(req, "website/gallery.html", {
        "active_page": "gallery",
        "gallery_hero": gallery_hero,
        "gallery_cta": gallery_cta,
        "wedding_header": wedding_header,
        "prewedding_header": prewedding_header,
        "birthday_header": birthday_header,
        "baby_header": baby_header,
        "events_header": events_header,
        "fashion_header": fashion_header,
        "portrait_header": portrait_header,
        "wedding_items": wedding_items,
        "prewedding_items": prewedding_items,
        "birthday_items": birthday_items,
        "baby_items": baby_items,
        "events_items": events_items,
        "fashion_items": fashion_items,
        "portrait_items": portrait_items,
    })



def contact(req):
    contact_hero = ContactHero.objects.last()
    if not contact_hero:
        contact_hero = ContactHero.objects.create(
            small_title="LET'S CREATE SOMETHING BEAUTIFUL",
            title="Contact Us",
            description="Have a special moment that you want to capture? We'd love to hear your story and create beautiful memories that you can cherish forever."
        )

    contact_info = ContactInfo.objects.last()
    if not contact_info:
        contact_info = ContactInfo.objects.create(
            phone="+91 98765 43210",
            email="info@photostudio.com",
            office_address="Pune, Maharashtra, India",
            whatsapp_number="+91 98765 43210",
            working_hours="Mon - Sat : 10:00 AM - 7:00 PM",
            google_map_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15133.486241951554!2d73.8567437!3d18.5204303!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c069e3288f3b%3A0x6b84733735166299!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
        )

    if req.method == "POST":
        full_name = req.POST.get("full_name", "").strip()
        email = req.POST.get("email", "").strip()
        phone = req.POST.get("phone", "").strip()
        service = req.POST.get("service", "").strip()
        event_date_str = req.POST.get("event_date", "").strip()
        message_text = req.POST.get("message", "").strip()

        event_date = None
        if event_date_str:
            try:
                event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d").date()
            except ValueError:
                pass

        if full_name and phone and message_text:
            ContactInquiry.objects.create(
                full_name=full_name,
                email=email or "not_provided@email.com",
                phone=phone,
                service=service or "General Inquiry",
                event_date=event_date,
                message=message_text
            )
            try:
                messages.success(req, "Thank you! Your inquiry has been sent successfully. Our team will contact you shortly.")
            except Exception:
                pass
            return redirect("/contact/#contactForm")
        else:
            try:
                messages.error(req, "Please fill in all required fields (Full Name, Phone, and Message).")
            except Exception:
                pass

    return render(req, "website/contact.html", {
        "active_page": "contact",
        "contact_hero": contact_hero,
        "contact_info": contact_info
    })

from django.http import JsonResponse

def check_date_availability(req):
    date_str = req.GET.get("date", "").strip()
    if not date_str:
        return JsonResponse({"available": False, "message": "No date specified."})

    is_booked = Booking.objects.filter(event_date=date_str).exclude(booking_status='Cancelled').exists()
    if is_booked:
        return JsonResponse({
            "available": False,
            "message": f"⚠️ Date {date_str} is ALREADY BOOKED! Please choose the next available date."
        })
    else:
        return JsonResponse({
            "available": True,
            "message": "✓ Date is available for booking!"
        })

def booking_form(req):
    if req.method == "POST":
        full_name = req.POST.get("full_name", "").strip()
        mobile = req.POST.get("mobile", "").strip()
        email = req.POST.get("email", "").strip()
        city = req.POST.get("city", "").strip()
        
        event_type = req.POST.get("event_type", "").strip()
        event_date = req.POST.get("event_date", "").strip()
        event_time = req.POST.get("event_time", "").strip()
        event_location = req.POST.get("event_location", "").strip()
        guests = req.POST.get("guests") or 1
        duration = req.POST.get("duration", "").strip()
        
        service = req.POST.get("service", "").strip()
        package = req.POST.get("package", "").strip()
        budget = req.POST.get("budget", "").strip()
        reference_image = req.FILES.get("reference_image")
        requirements = req.POST.get("requirements", "").strip()
        
        payment_method = req.POST.get("payment_method", "UPI").strip()
        advance_amount = req.POST.get("advance_amount", "0") or "0"
        transaction_id = req.POST.get("transaction_id", "").strip()
        
        # Check if date is already booked by another customer
        existing_booking = Booking.objects.filter(event_date=event_date).exclude(booking_status='Cancelled').first()
        if existing_booking:
            return render(req, "website/booking_form.html", {
                "date_error": f"The date ({event_date}) is ALREADY BOOKED for another photoshoot! Please select the next date.",
                "form_data": req.POST
            })

        password = req.POST.get("password", "").strip()
        
        booking = Booking.objects.create(
            full_name=full_name,
            mobile=mobile,
            email=email,
            city=city,
            password=password,
            event_type=event_type,
            event_date=event_date,
            event_time=event_time,
            event_location=event_location,
            guests=guests,
            duration=duration,
            service=service,
            package=package,
            budget=budget,
            reference_image=reference_image,
            requirements=requirements,
            payment_method=payment_method,
            advance_amount=advance_amount,
            payment_status="Paid" if transaction_id else "Pending",
            booking_status="Confirmed" if transaction_id else "Pending",
            transaction_id=transaction_id
        )
        
        import urllib.parse

        wa_message = f"""Hello {full_name}, तुमची photography booking confirm झाली आहे. 😊
तुमची booking successfully confirm केली आहे. Thank you! 🙏

📋 *Booking Summary:*
------------------------------
• *Booking ID:* #BK-{booking.id}890
• *Event Type:* {event_type}
• *Date & Time:* {event_date} at {event_time}
• *Venue:* {event_location}, {city}
• *Package:* {package or 'Standard Package'}
• *Advance Paid:* ₹{advance_amount} (SUCCESS)
• *TXN Ref:* {transaction_id}
------------------------------
A2Z Photographer Marketplace"""

        encoded_msg = urllib.parse.quote(wa_message)
        # WhatsApp URL for Customer
        whatsapp_url = f"https://api.whatsapp.com/send?phone=91{mobile}&text={encoded_msg}"
        # SMS URL (sms:phone?body=msg)
        sms_url = f"sms:+91{mobile}?body={encoded_msg}"

        return render(req, "website/booking_form.html", {
            "booking_success": True,
            "booking": booking,
            "whatsapp_url": whatsapp_url,
            "sms_url": sms_url
        })

    prefilled_service = req.GET.get("service", "").strip() or req.GET.get("event_type", "").strip() or req.GET.get("category", "").strip()
    return render(req, "website/booking_form.html", {
        "prefilled_service": prefilled_service
    })



# ── PAY REMAINING BALANCE PAGE ──
def pay_remaining(req, id):
    booking = Booking.objects.filter(id=id).first()
    if not booking:
        return redirect("/")

    total_price = booking.get_calculated_total_price()
    advance_paid = float(booking.advance_amount or 0)
    remaining_due = booking.get_remaining_due()

    if req.method == "POST":
        import time
        txn_id = req.POST.get("transaction_id", "").strip() or f"TXN{int(time.time())}"
        booking.remaining_amount = remaining_due
        booking.remaining_payment_status = "Paid"
        booking.remaining_txn_id = txn_id
        booking.payment_status = "Full Paid"
        booking.booking_status = "Completed"
        booking.save()

        import urllib.parse
        wa_message = f"""📸 *FULL PAYMENT RECEIPT - A2Z PHOTOGRAPHY* 📸

Hello {booking.full_name},
तुमची राहिलेली रक्कम (Remaining Balance) ₹{remaining_due:,.2f} यशस्वीरित्या जमा झाली आहे! 🙏

📋 *Final Payment Summary:*
------------------------------
• *Booking ID:* #BK-{booking.id}890
• *Customer:* {booking.full_name}
• *Event:* {booking.event_type}
• *Date & Time:* {booking.event_date} at {booking.event_time}
• *Total Package Amount:* ₹{total_price:,.2f}
• *Advance Paid:* ₹{advance_paid:,.2f} (Paid)
• *Remaining Paid:* ₹{remaining_due:,.2f} (SUCCESS)
• *Payment Status:* FULL PAID ✅
• *TXN Ref:* {txn_id}
------------------------------
Thank you for choosing A2Z Photographer Marketplace!"""

        encoded_msg = urllib.parse.quote(wa_message)
        whatsapp_url = f"https://api.whatsapp.com/send?phone=91{booking.mobile}&text={encoded_msg}"
        sms_url = f"sms:+91{booking.mobile}?body={encoded_msg}"

        return render(req, "website/pay_remaining.html", {
            "booking": booking,
            "total_price": total_price,
            "advance_paid": advance_paid,
            "remaining_due": 0.0,
            "payment_success": True,
            "whatsapp_url": whatsapp_url,
            "sms_url": sms_url
        })

    return render(req, "website/pay_remaining.html", {
        "booking": booking,
        "total_price": total_price,
        "advance_paid": advance_paid,
        "remaining_due": remaining_due
    })


# ── RAZORPAY PAYMENT GATEWAY API ──
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_razorpay_order(req):
    if req.method == "POST":
        import json, time
        try:
            data = json.loads(req.body)
        except Exception:
            data = req.POST
            
        amount = float(data.get("amount", 5000))
        amount_in_paisa = int(amount * 100)
        
        try:
            import razorpay
            from django.conf import settings
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            order_data = {
                "amount": amount_in_paisa,
                "currency": "INR",
                "payment_capture": 1
            }
            order = client.order.create(data=order_data)
            return JsonResponse({
                "success": True,
                "order_id": order.get("id"),
                "amount": amount,
                "key_id": settings.RAZORPAY_KEY_ID
            })
        except Exception as e:
            from django.conf import settings
            fake_order_id = f"order_rzp_{int(time.time())}"
            return JsonResponse({
                "success": True,
                "order_id": fake_order_id,
                "amount": amount,
                "key_id": getattr(settings, "RAZORPAY_KEY_ID", "rzp_test_A2ZPhotographerKey")
            })
            
    return JsonResponse({"error": "Invalid request method"}, status=400)


# ── CUSTOMER PORTAL VIEWS ──
def customer_login(req):
    error = None
    if req.method == "POST":
        email = req.POST.get("email", "").strip()
        password = req.POST.get("password", "").strip()

        if email and password:
            bookings = Booking.objects.filter(email__iexact=email, password=password)
            if not bookings.exists():
                # Allow fallback for earlier bookings created before password field
                bookings = Booking.objects.filter(email__iexact=email)

            if bookings.exists():
                req.session["customer_email"] = email
                return redirect("/my-bookings/")
            else:
                error = "Invalid Email Address or Password. Please check your login credentials."
        else:
            error = "Please enter both your registered Email Address and Password."

    return render(req, "website/customer_login.html", {"error": error})


def my_bookings(req):
    customer_email = req.session.get("customer_email")
    
    if req.GET.get("email"):
        customer_email = req.GET.get("email").strip()
        req.session["customer_email"] = customer_email

    if not customer_email:
        return redirect("/customer-login/")

    bookings = Booking.objects.filter(email__iexact=customer_email).order_by("-id")
    if not bookings.exists():
        req.session.pop("customer_email", None)
        return render(req, "website/customer_login.html", {
            "error": f"No active bookings found for email: {customer_email}"
        })

    first_booking = bookings.first()
    customer_name = first_booking.full_name if first_booking else "Customer"
    customer_mobile = first_booking.mobile if first_booking else ""

    total_bookings_count = bookings.count()
    total_paid_sum = sum(b.get_calculated_total_price() - b.get_remaining_due() for b in bookings)
    total_remaining_due_sum = sum(b.get_remaining_due() for b in bookings)

    return render(req, "website/my_bookings.html", {
        "active_page": "my_bookings",
        "customer_email": customer_email,
        "customer_mobile": customer_mobile,
        "customer_name": customer_name,
        "bookings": bookings,
        "total_bookings_count": total_bookings_count,
        "total_paid_sum": total_paid_sum,
        "total_remaining_due_sum": total_remaining_due_sum
    })


def customer_logout(req):
    req.session.pop("customer_email", None)
    return redirect("/customer-login/")


# ── FORGOT PASSWORD WITH OTP RESET VIEW ──
def forgot_password(req):
    step = req.POST.get("step", "send_otp")
    error = None
    success_msg = None

    reset_email = req.session.get("reset_email", "")
    reset_otp = req.session.get("reset_otp", "")

    # STEP 1: SEND OTP TO EMAIL
    if step == "send_otp" and req.method == "POST":
        email = req.POST.get("email", "").strip()
        if not email:
            error = "Please enter your registered Email Address."
        else:
            bookings = Booking.objects.filter(email__iexact=email)
            if not bookings.exists():
                error = f"No photoshoot booking found for email '{email}'. Please check your email."
            else:
                import random
                generated_otp = str(random.randint(100000, 999999))
                req.session["reset_email"] = email
                req.session["reset_otp"] = generated_otp
                req.session["otp_verified"] = False

                try:
                    from django.core.mail import send_mail
                    from django.conf import settings
                    send_mail(
                        subject="A2Z Photography - Password Reset OTP",
                        message=f"Your OTP for resetting your password is: {generated_otp}",
                        from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@photography.com'),
                        recipient_list=[email],
                        fail_silently=True
                    )
                except Exception:
                    pass

                step = "verify_otp"
                reset_email = email
                reset_otp = generated_otp
                success_msg = f"OTP sent to {email}! (Your Verification OTP is: {generated_otp})"

    # STEP 2: VERIFY OTP
    elif step == "verify_otp" and req.method == "POST":
        input_otp = req.POST.get("otp", "").strip()
        if input_otp and input_otp == str(reset_otp):
            req.session["otp_verified"] = True
            step = "reset_password"
            success_msg = "OTP Verified Successfully! Please enter your new password."
        else:
            step = "verify_otp"
            error = f"Invalid OTP entered. Please enter the 6-digit OTP sent to {reset_email}."

    # STEP 3: RESET NEW PASSWORD
    elif step == "reset_password" and req.method == "POST":
        new_password = req.POST.get("new_password", "").strip()
        confirm_password = req.POST.get("confirm_password", "").strip()

        if not new_password or not confirm_password:
            step = "reset_password"
            error = "Please fill in all password fields."
        elif new_password != confirm_password:
            step = "reset_password"
            error = "New Password and Confirm Password do not match. Please try again."
        else:
            Booking.objects.filter(email__iexact=reset_email).update(password=new_password)
            
            req.session.pop("reset_email", None)
            req.session.pop("reset_otp", None)
            req.session.pop("otp_verified", None)

            return render(req, "website/customer_login.html", {
                "success_msg": "Password updated successfully! Please login with your new password."
            })

    return render(req, "website/forgot_password.html", {
        "step": step,
        "reset_email": reset_email,
        "reset_otp": reset_otp,
        "error": error,
        "success_msg": success_msg
    })


# ── DEDICATED DIRECT PDF RECEIPT GENERATOR VIEW ──
def download_pdf_receipt(req, id):
    booking = Booking.objects.filter(id=id).first()
    if not booking:
        return redirect("/")

    total_price = booking.get_calculated_total_price()
    remaining_due = booking.get_remaining_due()
    advance_paid = max(0, total_price - remaining_due)

    return render(req, "website/pdf_receipt_download.html", {
        "booking": booking,
        "total_price": total_price,
        "advance_paid": advance_paid,
        "remaining_due": remaining_due
    })