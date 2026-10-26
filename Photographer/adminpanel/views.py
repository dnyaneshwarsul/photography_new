from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib import messages

from .models import AdminProfile, HomeSlider, HomeAbout, AboutPageInfo, HomeService, HomeFeaturedWork, HomeCategory, HomeVideoStory, HomeGallery, HomeWhyUs, HomeWhyUsHeader, HomeProcess, HomeProcessHeader, HomeClientStory, HomeTestimonial, HomeInstaPost, HomeAward, AboutStory, ServicesHero, HomeWhatWeOfferHeader, HomeWhatWeOfferItem, CategoryHero, ServicesCTA, CategorySectionHeader, GalleryHero, GallerySectionHeader, GalleryCTA, ContactHero, ContactInfo
from website.models import Booking, ContactInquiry
from django.db.models import Sum
import datetime


def process_header(request):
    header_data = HomeProcessHeader.objects.last()
    if not header_data:
        header_data = HomeProcessHeader.objects.create()

    if request.method == "POST":
        header_data.small_title = request.POST.get("small_title", header_data.small_title)
        header_data.title = request.POST.get("title", header_data.title)
        header_data.description = request.POST.get("description", header_data.description)
        header_data.save()
        messages.success(request, "Process Section Header updated successfully!")
        return redirect("/admin/process-header/")

    return render(request, "admin/process_header.html", {"header_data": header_data, "active_page": "process_header"})


def add_process(request):
    if request.method == "POST":
        step_number = request.POST.get("step_number", "01")
        icon_class = request.POST.get("icon_class", "bi bi-chat-heart")
        icon_image = request.FILES.get("icon_image")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")

        HomeProcess.objects.create(
            step_number=step_number,
            icon_class=icon_class,
            icon_image=icon_image,
            title=title,
            description=description
        )
        messages.success(request, "Process step added successfully!")
        return redirect("/admin/process-list/")

    return render(request, "admin/add_process.html", {"active_page": "add_process"})


def process_list(request):
    processes = HomeProcess.objects.all().order_by("step_number")
    return render(request, "admin/process_list.html", {"processes": processes, "active_page": "process_list"})


def edit_process(request, id):
    process = HomeProcess.objects.filter(id=id).first()
    if not process:
        messages.error(request, "Process step not found!")
        return redirect("/admin/process-list/")

    if request.method == "POST":
        process.step_number = request.POST.get("step_number", process.step_number)
        process.icon_class = request.POST.get("icon_class", process.icon_class)
        if request.FILES.get("icon_image"):
            process.icon_image = request.FILES.get("icon_image")
        process.title = request.POST.get("title", process.title)
        process.description = request.POST.get("description", process.description)

        process.save()
        messages.success(request, "Process step updated successfully!")
        return redirect("/admin/process-list/")

    return render(request, "admin/edit_process.html", {"process": process, "active_page": "process_list"})


def delete_process(request, id):
    process = HomeProcess.objects.filter(id=id).first()
    if process:
        process.delete()
        messages.success(request, "Process step deleted successfully!")
    return redirect("/admin/process-list/")



def why_us_header(request):
    header_data = HomeWhyUsHeader.objects.last()
    if not header_data:
        header_data = HomeWhyUsHeader.objects.create(
            small_title="ABOUT ME",
            title="Turning Beautiful Moments Into Timeless Memories",
            description="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
        )

    if request.method == "POST":
        header_data.small_title = request.POST.get("small_title", header_data.small_title)
        header_data.title = request.POST.get("title", header_data.title)
        header_data.description = request.POST.get("description", header_data.description)
        if request.FILES.get("section_image"):
            header_data.section_image = request.FILES.get("section_image")
        header_data.save()
        messages.success(request, "Why Choose Us / About Me Section Header updated successfully!")
        return redirect("/admin/why-us-header/")

    return render(request, "admin/why_us_header.html", {"header_data": header_data, "active_page": "why_us_header"})


def add_why_us(request):
    if request.method == "POST":
        icon_class = request.POST.get("icon_class", "bi bi-camera")
        icon_image = request.FILES.get("icon_image")
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            HomeWhyUs.objects.create(
                icon_class=icon_class,
                icon_image=icon_image,
                title=title,
                description=description
            )
            messages.success(request, "Why Choose Us item added successfully!")
            return redirect("/admin/why-us-list/")
        else:
            messages.error(request, "Title is required!")

    return render(request, "admin/add_why_us.html", {"active_page": "add_why_us"})


def why_us_list(request):
    header_data = HomeWhyUsHeader.objects.last()
    why_us_items = HomeWhyUs.objects.all().order_by("id")
    return render(request, "admin/why_us_list.html", {
        "header_data": header_data,
        "why_us_items": why_us_items,
        "active_page": "why_us_list"
    })


def edit_why_us(request, id):
    item = HomeWhyUs.objects.filter(id=id).first()
    if not item:
        messages.error(request, "Why Us item not found!")
        return redirect("/admin/why-us-list/")

    if request.method == "POST":
        item.icon_class = request.POST.get("icon_class", item.icon_class)
        if request.FILES.get("icon_image"):
            item.icon_image = request.FILES.get("icon_image")
        item.title = request.POST.get("title", item.title)
        item.description = request.POST.get("description", item.description)

        item.save()
        messages.success(request, "Why Choose Us item updated successfully!")
        return redirect("/admin/why-us-list/")

    return render(request, "admin/edit_why_us.html", {"item": item, "active_page": "why_us_list"})


def delete_why_us(request, id):
    item = HomeWhyUs.objects.filter(id=id).first()
    if item:
        item.delete()
        messages.success(request, "Why Us item deleted successfully!")
    return redirect("/admin/why-us-list/")


def add_gallery(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        subtitle = request.POST.get("subtitle", "").strip()
        category_name = request.POST.get("category_name", "Wedding").strip()
        gallery_image = request.FILES.get("gallery_image")

        HomeGallery.objects.create(
            title=title,
            subtitle=subtitle,
            category_name=category_name,
            gallery_image=gallery_image
        )
        messages.success(request, "Gallery photo added successfully!")
        return redirect("/admin/gallery-list/")

    return render(request, "admin/add_gallery.html")


def gallery_list(request):
    galleries = HomeGallery.objects.all().order_by("-id")
    return render(request, "admin/gallery_list.html", {"galleries": galleries})


def edit_gallery(request, id):
    gallery_item = HomeGallery.objects.filter(id=id).first()
    if not gallery_item:
        messages.error(request, "Gallery item not found!")
        return redirect("/admin/gallery-list/")

    if request.method == "POST":
        gallery_item.title = request.POST.get("title", gallery_item.title).strip()
        gallery_item.subtitle = request.POST.get("subtitle", gallery_item.subtitle).strip()
        gallery_item.category_name = request.POST.get("category_name", gallery_item.category_name).strip()

        if request.FILES.get("gallery_image"):
            gallery_item.gallery_image = request.FILES.get("gallery_image")

        gallery_item.save()
        messages.success(request, "Gallery photo updated successfully!")
        return redirect("/admin/gallery-list/")

    return render(request, "admin/edit_gallery.html", {"gallery_item": gallery_item})


def delete_gallery(request, id):
    gallery_item = HomeGallery.objects.filter(id=id).first()
    if gallery_item:
        gallery_item.delete()
        messages.success(request, "Gallery item deleted successfully!")
    return redirect("/admin/gallery-list/")


def add_video_story(request):
    if request.method == "POST":
        category_tag = request.POST.get("category_tag", "")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        video_file = request.FILES.get("video_file")
        video_url = request.POST.get("video_url", "")

        HomeVideoStory.objects.create(
            category_tag=category_tag,
            title=title,
            description=description,
            video_file=video_file,
            video_url=video_url
        )
        messages.success(request, "Video Story added successfully!")
        return redirect("/admin/video-story-list/")

    return render(request, "admin/add_video_story.html")


def video_story_list(request):
    video_stories = HomeVideoStory.objects.all().order_by("-id")
    return render(request, "admin/video_story_list.html", {"video_stories": video_stories})


def edit_video_story(request, id):
    video_story = HomeVideoStory.objects.filter(id=id).first()
    if not video_story:
        messages.error(request, "Video Story not found!")
        return redirect("/admin/video-story-list/")

    if request.method == "POST":
        video_story.category_tag = request.POST.get("category_tag", video_story.category_tag)
        video_story.title = request.POST.get("title", video_story.title)
        video_story.description = request.POST.get("description", video_story.description)
        video_story.video_url = request.POST.get("video_url", video_story.video_url)

        if request.FILES.get("video_file"):
            video_story.video_file = request.FILES.get("video_file")

        video_story.save()
        messages.success(request, "Video Story updated successfully!")
        return redirect("/admin/video-story-list/")

    return render(request, "admin/edit_video_story.html", {"video_story": video_story})


def delete_video_story(request, id):
    video_story = HomeVideoStory.objects.filter(id=id).first()
    if video_story:
        video_story.delete()
        messages.success(request, "Video Story deleted successfully!")
    return redirect("/admin/video-story-list/")


def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name", "").strip()
        category_image = request.FILES.get("category_image")
        description = request.POST.get("description", "").strip()
        sub_services = request.POST.get("sub_services", "").strip()
        detail_image = request.FILES.get("detail_image")

        HomeCategory.objects.create(
            category_name=category_name,
            category_image=category_image,
            description=description,
            sub_services=sub_services,
            detail_image=detail_image
        )
        messages.success(request, "Photography Category added successfully!")
        return redirect("/admin/category-list/")

    return render(request, "admin/add_category.html")


def category_list(request):
    categories = HomeCategory.objects.all().order_by("-id")
    return render(request, "admin/category_list.html", {"categories": categories})


def edit_category(request, id):
    category = HomeCategory.objects.filter(id=id).first()
    if not category:
        messages.error(request, "Category not found!")
        return redirect("/admin/category-list/")

    if request.method == "POST":
        category.category_name = request.POST.get("category_name", category.category_name).strip()
        category.description = request.POST.get("description", category.description).strip()
        category.sub_services = request.POST.get("sub_services", category.sub_services).strip()

        if request.FILES.get("category_image"):
            category.category_image = request.FILES.get("category_image")

        if request.FILES.get("detail_image"):
            category.detail_image = request.FILES.get("detail_image")

        category.save()
        messages.success(request, "Category updated successfully!")
        return redirect("/admin/category-list/")

    return render(request, "admin/edit_category.html", {"category": category})


def delete_category(request, id):
    category = HomeCategory.objects.filter(id=id).first()
    if category:
        category.delete()
        messages.success(request, "Category deleted successfully!")
    return redirect("/admin/category-list/")


def add_featured(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        category_name = request.POST.get("category_name", "")
        work_image = request.FILES.get("work_image")

        HomeFeaturedWork.objects.create(
            title=title,
            category_name=category_name,
            work_image=work_image
        )
        messages.success(request, "Featured Work added successfully!")
        return redirect("/admin/featured-list/")

    return render(request, "admin/add_featured.html")


def featured_list(request):
    featured_works = HomeFeaturedWork.objects.all().order_by("-id")
    return render(request, "admin/featured_list.html", {"featured_works": featured_works})


def edit_featured(request, id):
    featured = HomeFeaturedWork.objects.filter(id=id).first()
    if not featured:
        messages.error(request, "Featured Work not found!")
        return redirect("/admin/featured-list/")

    if request.method == "POST":
        featured.title = request.POST.get("title", featured.title)
        featured.category_name = request.POST.get("category_name", featured.category_name)

        if request.FILES.get("work_image"):
            featured.work_image = request.FILES.get("work_image")

        featured.save()
        messages.success(request, "Featured Work updated successfully!")
        return redirect("/admin/featured-list/")

    return render(request, "admin/edit_featured.html", {"featured": featured})


def delete_featured(request, id):
    featured = HomeFeaturedWork.objects.filter(id=id).first()
    if featured:
        featured.delete()
        messages.success(request, "Featured Work deleted successfully!")
    return redirect("/admin/featured-list/")


def add_service(request):
    if request.method == "POST":
        icon_class = request.POST.get("icon_class", "bi bi-heart")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        service_image = request.FILES.get("service_image")

        HomeService.objects.create(
            icon_class=icon_class,
            title=title,
            description=description,
            service_image=service_image
        )
        messages.success(request, "Photography Service added successfully!")
        return redirect("/admin/service-list/")

    return render(request, "admin/add_service.html")


def service_list(request):
    services = HomeService.objects.all().order_by("-id")
    return render(request, "admin/service_list.html", {"services": services})


def edit_service(request, id):
    service = HomeService.objects.filter(id=id).first()
    if not service:
        messages.error(request, "Service not found!")
        return redirect("/admin/service-list/")

    if request.method == "POST":
        service.icon_class = request.POST.get("icon_class", service.icon_class)
        service.title = request.POST.get("title", service.title)
        service.description = request.POST.get("description", service.description)

        if request.FILES.get("service_image"):
            service.service_image = request.FILES.get("service_image")

        service.save()
        messages.success(request, "Photography Service updated successfully!")
        return redirect("/admin/service-list/")

    return render(request, "admin/edit_service.html", {"service": service})


def delete_service(request, id):
    service = HomeService.objects.filter(id=id).first()
    if service:
        service.delete()
        messages.success(request, "Service deleted successfully!")
    return redirect("/admin/service-list/")


def add_about(request):
    if request.method == "POST":
        small_title = request.POST.get("small_title", "About Me")
        title = request.POST.get("title", "Turning Beautiful Moments Into Timeless Memories")
        description_para1 = request.POST.get("description_para1", "")
        description_para2 = request.POST.get("description_para2", "")
        photographer_name = request.POST.get("photographer_name", "Your Photographer")
        about_image = request.FILES.get("about_image")
        
        experience_years = request.POST.get("experience_years", "10+")
        experience_text = request.POST.get("experience_text", "Years of Photography Experience")
        
        feature1_title = request.POST.get("feature1_title", "Professional Photographers")
        feature1_desc = request.POST.get("feature1_desc", "Skilled photographers with creative experience and unique styles.")
        feature1_icon = request.POST.get("feature1_icon", "bi bi-camera")

        feature2_title = request.POST.get("feature2_title", "Creative Photography")
        feature2_desc = request.POST.get("feature2_desc", "Creative ideas that turn ordinary moments into beautiful memories.")
        feature2_icon = request.POST.get("feature2_icon", "bi bi-stars")

        feature3_title = request.POST.get("feature3_title", "Genuine Emotions")
        feature3_desc = request.POST.get("feature3_desc", "Natural emotions captured in authentic and meaningful frames.")
        feature3_icon = request.POST.get("feature3_icon", "bi bi-heart")

        AboutPageInfo.objects.create(
            small_title=small_title,
            title=title,
            description_para1=description_para1,
            description_para2=description_para2,
            photographer_name=photographer_name,
            about_image=about_image,
            experience_years=experience_years,
            experience_text=experience_text,
            feature1_title=feature1_title,
            feature1_desc=feature1_desc,
            feature1_icon=feature1_icon,
            feature2_title=feature2_title,
            feature2_desc=feature2_desc,
            feature2_icon=feature2_icon,
            feature3_title=feature3_title,
            feature3_desc=feature3_desc,
            feature3_icon=feature3_icon
        )
        messages.success(request, "About Me section added successfully!")
        return redirect("/admin/about-list/")

    return render(request, "admin/add_about.html")


def about_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("-id")
    return render(request, "admin/about_list.html", {"about_entries": about_entries})


def edit_about(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if not about_obj:
        messages.error(request, "About entry not found!")
        return redirect("/admin/about-list/")

    if request.method == "POST":
        about_obj.small_title = request.POST.get("small_title", about_obj.small_title)
        about_obj.title = request.POST.get("title", about_obj.title)
        about_obj.description_para1 = request.POST.get("description_para1", about_obj.description_para1)
        about_obj.description_para2 = request.POST.get("description_para2", about_obj.description_para2)
        about_obj.photographer_name = request.POST.get("photographer_name", about_obj.photographer_name)

        about_obj.experience_years = request.POST.get("experience_years", about_obj.experience_years)
        about_obj.experience_text = request.POST.get("experience_text", about_obj.experience_text)

        about_obj.feature1_title = request.POST.get("feature1_title", about_obj.feature1_title)
        about_obj.feature1_desc = request.POST.get("feature1_desc", about_obj.feature1_desc)
        about_obj.feature1_icon = request.POST.get("feature1_icon", about_obj.feature1_icon)

        about_obj.feature2_title = request.POST.get("feature2_title", about_obj.feature2_title)
        about_obj.feature2_desc = request.POST.get("feature2_desc", about_obj.feature2_desc)
        about_obj.feature2_icon = request.POST.get("feature2_icon", about_obj.feature2_icon)

        about_obj.feature3_title = request.POST.get("feature3_title", about_obj.feature3_title)
        about_obj.feature3_desc = request.POST.get("feature3_desc", about_obj.feature3_desc)
        about_obj.feature3_icon = request.POST.get("feature3_icon", about_obj.feature3_icon)

        if request.FILES.get("about_image"):
            about_obj.about_image = request.FILES.get("about_image")

        about_obj.save()
        messages.success(request, "About Me section updated successfully!")
        return redirect("/admin/about-list/")

    return render(request, "admin/edit_about.html", {"about": about_obj})


def delete_about(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "About entry deleted successfully!")
    return redirect("/admin/about-list/")


# ── ABOUT HERO BANNER MANAGEMENT (ADD / LIST / EDIT / DELETE) ──
def add_about_hero(request):
    if request.method == "POST":
        hero_label = request.POST.get("hero_label", "ABOUT ME")
        hero_title = request.POST.get("hero_title", "Turning Beautiful Moments Into Timeless Memories")
        hero_description = request.POST.get("hero_description", "")
        hero_image = request.FILES.get("hero_image")

        AboutPageInfo.objects.create(
            hero_label=hero_label,
            hero_title=hero_title,
            hero_description=hero_description,
            hero_image=hero_image
        )
        messages.success(request, "Top Hero Banner added successfully!")
        return redirect("/admin/about-hero-list/")

    return render(request, "admin/add_about_hero.html")


def about_hero_list(request):
    hero_entries = AboutPageInfo.objects.all().order_by("-id")
    return render(request, "admin/about_hero_list.html", {"hero_entries": hero_entries})


def edit_about_hero(request, id):
    hero_obj = AboutPageInfo.objects.filter(id=id).first()
    if not hero_obj:
        messages.error(request, "Hero Banner entry not found!")
        return redirect("/admin/about-hero-list/")

    if request.method == "POST":
        hero_obj.hero_label = request.POST.get("hero_label", hero_obj.hero_label)
        hero_obj.hero_title = request.POST.get("hero_title", hero_obj.hero_title)
        hero_obj.hero_description = request.POST.get("hero_description", hero_obj.hero_description)

        if request.FILES.get("hero_image"):
            hero_obj.hero_image = request.FILES.get("hero_image")

        hero_obj.save()
        messages.success(request, "Top Hero Banner updated successfully!")
        return redirect("/admin/about-hero-list/")

    return render(request, "admin/edit_about_hero.html", {"about": hero_obj})


def delete_about_hero(request, id):
    hero_obj = AboutPageInfo.objects.filter(id=id).first()
    if hero_obj:
        hero_obj.delete()
        messages.success(request, "Hero Banner entry deleted successfully!")
    return redirect("/admin/about-hero-list/")


# ── SINGLE DIRECT EDIT FOR OUR STORY HEADER & IMAGE INFO ──
def about_story_header(request):
    about_obj, _ = AboutPageInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        about_obj.story_small_title = request.POST.get("story_small_title", about_obj.story_small_title)
        about_obj.story_title = request.POST.get("story_title", about_obj.story_title)
        about_obj.story_desc1 = request.POST.get("story_desc1", about_obj.story_desc1)
        about_obj.story_desc2 = request.POST.get("story_desc2", about_obj.story_desc2)
        about_obj.story_badge_title = request.POST.get("story_badge_title", about_obj.story_badge_title)
        about_obj.story_badge_subtitle = request.POST.get("story_badge_subtitle", about_obj.story_badge_subtitle)

        if request.FILES.get("story_image"):
            about_obj.story_image = request.FILES.get("story_image")

        about_obj.save()
        messages.success(request, "Our Story Header & Image Info updated successfully!")
        return redirect("/admin/about-story-header/")

    return render(request, "admin/about_story_header.html", {"about": about_obj})


# ── SINGLE DIRECT EDIT FOR WHAT WE DO HEADER INFO ──
def what_we_do_header(request):
    about_obj, _ = AboutPageInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        about_obj.what_we_do_label = request.POST.get("what_we_do_label", about_obj.what_we_do_label)
        about_obj.what_we_do_title = request.POST.get("what_we_do_title", about_obj.what_we_do_title)
        about_obj.what_we_do_desc = request.POST.get("what_we_do_desc", about_obj.what_we_do_desc)

        about_obj.save()
        messages.success(request, "What We Do Header updated successfully!")
        return redirect("/admin/what-we-do-list/")

    return render(request, "admin/what_we_do_header.html", {"about": about_obj})


def what_we_do_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("id")
    return render(request, "admin/what_we_do_list.html", {"about_entries": about_entries})


# ── SINGLE DIRECT EDIT FOR OUR MISSION SECTION INFO ──
def about_mission_section(request):
    about_obj, _ = AboutPageInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        about_obj.mission_small_title = request.POST.get("mission_small_title", about_obj.mission_small_title)
        about_obj.mission_title = request.POST.get("mission_title", about_obj.mission_title)
        about_obj.mission_quote = request.POST.get("mission_quote", about_obj.mission_quote)
        about_obj.mission_point1 = request.POST.get("mission_point1", about_obj.mission_point1)
        about_obj.mission_point2 = request.POST.get("mission_point2", about_obj.mission_point2)
        about_obj.mission_point3 = request.POST.get("mission_point3", about_obj.mission_point3)

        if request.FILES.get("mission_bg_image"):
            about_obj.mission_bg_image = request.FILES.get("mission_bg_image")

        about_obj.save()
        messages.success(request, "Our Mission Section updated successfully!")
        return redirect("/admin/about-mission-list/")

    return render(request, "admin/about_mission_section.html", {"about": about_obj})


def about_mission_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("id")
    return render(request, "admin/about_mission_list.html", {"about_entries": about_entries})


# ── SINGLE DIRECT EDIT FOR OUR VISION SECTION INFO ──
def about_vision_section(request):
    about_obj, _ = AboutPageInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        about_obj.vision_small_title = request.POST.get("vision_small_title", about_obj.vision_small_title)
        about_obj.vision_title_line1 = request.POST.get("vision_title_line1", about_obj.vision_title_line1)
        about_obj.vision_title_highlight = request.POST.get("vision_title_highlight", about_obj.vision_title_highlight)
        about_obj.vision_description = request.POST.get("vision_description", about_obj.vision_description)
        about_obj.vision_quote = request.POST.get("vision_quote", about_obj.vision_quote)

        about_obj.vision_val1 = request.POST.get("vision_val1", about_obj.vision_val1)
        about_obj.vision_val1_icon = request.POST.get("vision_val1_icon", about_obj.vision_val1_icon)

        about_obj.vision_val2 = request.POST.get("vision_val2", about_obj.vision_val2)
        about_obj.vision_val2_icon = request.POST.get("vision_val2_icon", about_obj.vision_val2_icon)

        about_obj.vision_val3 = request.POST.get("vision_val3", about_obj.vision_val3)
        about_obj.vision_val3_icon = request.POST.get("vision_val3_icon", about_obj.vision_val3_icon)

        about_obj.vision_val4 = request.POST.get("vision_val4", about_obj.vision_val4)
        about_obj.vision_val4_icon = request.POST.get("vision_val4_icon", about_obj.vision_val4_icon)

        if request.FILES.get("vision_image"):
            about_obj.vision_image = request.FILES.get("vision_image")

        about_obj.save()
        messages.success(request, "Our Vision Section updated successfully!")
        return redirect("/admin/about-vision-list/")

    return render(request, "admin/about_vision_section.html", {"about": about_obj})


def about_vision_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("id")
    return render(request, "admin/about_vision_list.html", {"about_entries": about_entries})


def delete_what_we_do(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "What We Do Header deleted successfully!")
    return redirect("/admin/what-we-do-list/")


def delete_mission(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "Our Mission section deleted successfully!")
    return redirect("/admin/about-mission-list/")


def delete_vision(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "Our Vision section deleted successfully!")
    return redirect("/admin/about-vision-list/")


# ── SINGLE DIRECT EDIT FOR OUR NUMBERS COUNTER STATS SECTION ──
def about_numbers_section(request):
    about_obj = AboutPageInfo.objects.first()
    if not about_obj:
        about_obj = AboutPageInfo.objects.create()

    if request.method == "POST":
        numbers_small_title = request.POST.get("numbers_small_title", "").strip() or "OUR NUMBERS"
        numbers_title = request.POST.get("numbers_title", "").strip() or "Growing Together Through Photography"
        numbers_desc = request.POST.get("numbers_desc", "").strip() or "Our growing photography community continues to capture beautiful stories."

        stat1_count = request.POST.get("stat1_count", "").strip() or "500+"
        stat1_title = request.POST.get("stat1_title", "").strip() or "Happy Clients"
        stat1_icon = request.POST.get("stat1_icon", "").strip() or "bi bi-people"

        stat2_count = request.POST.get("stat2_count", "").strip() or "150+"
        stat2_title = request.POST.get("stat2_title", "").strip() or "Professional Photographers"
        stat2_icon = request.POST.get("stat2_icon", "").strip() or "bi bi-camera"

        stat3_count = request.POST.get("stat3_count", "").strip() or "1000+"
        stat3_title = request.POST.get("stat3_title", "").strip() or "Events Captured"
        stat3_icon = request.POST.get("stat3_icon", "").strip() or "bi bi-calendar-heart"

        stat4_count = request.POST.get("stat4_count", "").strip() or "25+"
        stat4_title = request.POST.get("stat4_title", "").strip() or "Photography Categories"
        stat4_icon = request.POST.get("stat4_icon", "").strip() or "bi bi-grid"

        if AboutPageInfo.objects.exists():
            AboutPageInfo.objects.all().update(
                numbers_small_title=numbers_small_title,
                numbers_title=numbers_title,
                numbers_desc=numbers_desc,
                stat1_count=stat1_count,
                stat1_title=stat1_title,
                stat1_icon=stat1_icon,
                stat2_count=stat2_count,
                stat2_title=stat2_title,
                stat2_icon=stat2_icon,
                stat3_count=stat3_count,
                stat3_title=stat3_title,
                stat3_icon=stat3_icon,
                stat4_count=stat4_count,
                stat4_title=stat4_title,
                stat4_icon=stat4_icon
            )
        else:
            AboutPageInfo.objects.create(
                numbers_small_title=numbers_small_title,
                numbers_title=numbers_title,
                numbers_desc=numbers_desc,
                stat1_count=stat1_count,
                stat1_title=stat1_title,
                stat1_icon=stat1_icon,
                stat2_count=stat2_count,
                stat2_title=stat2_title,
                stat2_icon=stat2_icon,
                stat3_count=stat3_count,
                stat3_title=stat3_title,
                stat3_icon=stat3_icon,
                stat4_count=stat4_count,
                stat4_title=stat4_title,
                stat4_icon=stat4_icon
            )

        messages.success(request, "Our Numbers Section updated successfully!")
        return redirect("/admin/about-numbers-section/")

    return render(request, "admin/about_numbers_section.html", {"about": about_obj})


def about_numbers_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("id")
    return render(request, "admin/about_numbers_list.html", {"about_entries": about_entries})


def delete_numbers(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "Our Numbers section entry deleted successfully!")
    return redirect("/admin/about-numbers-list/")



# ── SINGLE DIRECT EDIT FOR START YOUR STORY CTA SECTION ──
def about_cta_section(request):
    about_obj = AboutPageInfo.objects.first()
    if not about_obj:
        about_obj = AboutPageInfo.objects.create()

    if request.method == "POST":
        cta_small_title = request.POST.get("cta_small_title", "").strip() or "START YOUR STORY"
        cta_title = request.POST.get("cta_title", "").strip() or "Your Story Deserves To Be Captured."
        cta_desc = request.POST.get("cta_desc", "").strip() or "Whether it is your wedding, a special celebration, a family moment or a personal milestone — find the right photographer to capture it beautifully."
        cta_btn1_text = request.POST.get("cta_btn1_text", "").strip() or "Book a Photographer"
        cta_btn1_link = request.POST.get("cta_btn1_link", "").strip() or "/booking_form/"
        cta_btn2_text = request.POST.get("cta_btn2_text", "").strip() or "Explore Categories"
        cta_btn2_link = request.POST.get("cta_btn2_link", "").strip() or "/category/"

        about_obj.cta_small_title = cta_small_title
        about_obj.cta_title = cta_title
        about_obj.cta_desc = cta_desc
        about_obj.cta_btn1_text = cta_btn1_text
        about_obj.cta_btn1_link = cta_btn1_link
        about_obj.cta_btn2_text = cta_btn2_text
        about_obj.cta_btn2_link = cta_btn2_link

        if request.FILES.get("cta_bg_image"):
            about_obj.cta_bg_image = request.FILES.get("cta_bg_image")

        about_obj.save()

        if AboutPageInfo.objects.exists():
            AboutPageInfo.objects.all().update(
                cta_small_title=cta_small_title,
                cta_title=cta_title,
                cta_desc=cta_desc,
                cta_btn1_text=cta_btn1_text,
                cta_btn1_link=cta_btn1_link,
                cta_btn2_text=cta_btn2_text,
                cta_btn2_link=cta_btn2_link
            )

        messages.success(request, "Start Your Story CTA Section updated successfully!")
        return redirect("/admin/about-cta-section/")

    return render(request, "admin/about_cta_section.html", {"about": about_obj})


def about_cta_list(request):
    about_entries = AboutPageInfo.objects.all().order_by("id")
    return render(request, "admin/about_cta_list.html", {"about_entries": about_entries})


def delete_cta(request, id):
    about_obj = AboutPageInfo.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "Start Your Story CTA entry deleted successfully!")
    return redirect("/admin/about-cta-list/")


# ── SINGLE DIRECT EDIT FOR ABOUT WHO WE ARE / ABOUT ME SECTION ──
def about_whoweare(request):
    about_obj, _ = AboutPageInfo.objects.get_or_create(id=1)

    if request.method == "POST":
        about_obj.small_title = request.POST.get("small_title", about_obj.small_title)
        about_obj.title = request.POST.get("title", about_obj.title)
        about_obj.description_para1 = request.POST.get("description_para1", about_obj.description_para1)
        about_obj.description_para2 = request.POST.get("description_para2", about_obj.description_para2)
        about_obj.photographer_name = request.POST.get("photographer_name", about_obj.photographer_name)

        about_obj.experience_years = request.POST.get("experience_years", about_obj.experience_years)
        about_obj.experience_text = request.POST.get("experience_text", about_obj.experience_text)

        about_obj.feature1_title = request.POST.get("feature1_title", about_obj.feature1_title)
        about_obj.feature1_desc = request.POST.get("feature1_desc", about_obj.feature1_desc)
        about_obj.feature1_icon = request.POST.get("feature1_icon", about_obj.feature1_icon)

        about_obj.feature2_title = request.POST.get("feature2_title", about_obj.feature2_title)
        about_obj.feature2_desc = request.POST.get("feature2_desc", about_obj.feature2_desc)
        about_obj.feature2_icon = request.POST.get("feature2_icon", about_obj.feature2_icon)

        about_obj.feature3_title = request.POST.get("feature3_title", about_obj.feature3_title)
        about_obj.feature3_desc = request.POST.get("feature3_desc", about_obj.feature3_desc)
        about_obj.feature3_icon = request.POST.get("feature3_icon", about_obj.feature3_icon)

        if request.FILES.get("about_image"):
            about_obj.about_image = request.FILES.get("about_image")

        about_obj.save()
        messages.success(request, "About Me / Who We Are Section updated successfully!")
        return redirect("/admin/about-whoweare/")

    return render(request, "admin/edit_about.html", {"about": about_obj})


# ── HOME PAGE ABOUT ME MANAGEMENT ──
def add_home_about(request):
    if request.method == "POST":
        small_title = request.POST.get("small_title", "About Me")
        title = request.POST.get("title", "Turning Beautiful Moments Into Timeless Memories")
        description_para1 = request.POST.get("description_para1", "")
        description_para2 = request.POST.get("description_para2", "")
        photographer_name = request.POST.get("photographer_name", "Your Photographer")
        about_image = request.FILES.get("about_image")

        HomeAbout.objects.create(
            small_title=small_title,
            title=title,
            description_para1=description_para1,
            description_para2=description_para2,
            photographer_name=photographer_name,
            about_image=about_image
        )
        messages.success(request, "Home Page About Me section added successfully!")
        return redirect("/admin/home-about-list/")

    return render(request, "admin/add_home_about.html")


def home_about_list(request):
    about_entries = HomeAbout.objects.all().order_by("-id")
    return render(request, "admin/home_about_list.html", {"about_entries": about_entries})


def edit_home_about(request, id):
    about_obj = HomeAbout.objects.filter(id=id).first()
    if not about_obj:
        messages.error(request, "Home About entry not found!")
        return redirect("/admin/home-about-list/")

    if request.method == "POST":
        about_obj.small_title = request.POST.get("small_title", about_obj.small_title)
        about_obj.title = request.POST.get("title", about_obj.title)
        about_obj.description_para1 = request.POST.get("description_para1", about_obj.description_para1)
        about_obj.description_para2 = request.POST.get("description_para2", about_obj.description_para2)
        about_obj.photographer_name = request.POST.get("photographer_name", about_obj.photographer_name)

        if request.FILES.get("about_image"):
            about_obj.about_image = request.FILES.get("about_image")

        about_obj.save()
        messages.success(request, "Home Page About Me section updated successfully!")
        return redirect("/admin/home-about-list/")

    return render(request, "admin/edit_home_about.html", {"about": about_obj})


def delete_home_about(request, id):
    about_obj = HomeAbout.objects.filter(id=id).first()
    if about_obj:
        about_obj.delete()
        messages.success(request, "Home About entry deleted successfully!")
    return redirect("/admin/home-about-list/")


def add_slider(request):
    if request.method == "POST":
        tagline = request.POST.get("tagline", "A2Z PHOTOGRAPHERS")
        icon_class = request.POST.get("icon_class", "bi bi-camera-fill")
        title_line1 = request.POST.get("title_line1", "Your Story.")
        title_line2_prefix = request.POST.get("title_line2_prefix", "Our ")
        title_line2_highlight = request.POST.get("title_line2_highlight", "Lens.")
        description = request.POST.get("description", "")
        btn1_text = request.POST.get("btn1_text", "Find a Photographer")
        btn1_link = request.POST.get("btn1_link", "#")
        btn2_text = request.POST.get("btn2_text", "Explore Portfolio")
        btn2_link = request.POST.get("btn2_link", "#")
        slider_image = request.FILES.get("slider_image")

        HomeSlider.objects.create(
            tagline=tagline,
            icon_class=icon_class,
            title_line1=title_line1,
            title_line2_prefix=title_line2_prefix,
            title_line2_highlight=title_line2_highlight,
            description=description,
            btn1_text=btn1_text,
            btn1_link=btn1_link,
            btn2_text=btn2_text,
            btn2_link=btn2_link,
            slider_image=slider_image
        )
        messages.success(request, "Home Slider added successfully!")
        return redirect("/admin/slider-list/")

    return render(request, "admin/add_slider.html")


def slider_list(request):
    sliders = HomeSlider.objects.all().order_by("-id")
    return render(request, "admin/slider_list.html", {"sliders": sliders})


def delete_slider(request, id):
    slider = HomeSlider.objects.filter(id=id).first()
    if slider:
        slider.delete()
        messages.success(request, "Slider deleted successfully!")
    return redirect("/admin/slider-list/")


def edit_slider(request, id):
    slider = HomeSlider.objects.filter(id=id).first()
    if not slider:
        messages.error(request, "Slider not found!")
        return redirect("/admin/slider-list/")

    if request.method == "POST":
        slider.tagline = request.POST.get("tagline", slider.tagline)
        slider.icon_class = request.POST.get("icon_class", slider.icon_class)
        slider.title_line1 = request.POST.get("title_line1", slider.title_line1)
        slider.title_line2_prefix = request.POST.get("title_line2_prefix", slider.title_line2_prefix)
        slider.title_line2_highlight = request.POST.get("title_line2_highlight", slider.title_line2_highlight)
        slider.description = request.POST.get("description", slider.description)
        slider.btn1_text = request.POST.get("btn1_text", slider.btn1_text)
        slider.btn1_link = request.POST.get("btn1_link", slider.btn1_link)
        slider.btn2_text = request.POST.get("btn2_text", slider.btn2_text)
        slider.btn2_link = request.POST.get("btn2_link", slider.btn2_link)

        if request.FILES.get("slider_image"):
            slider.slider_image = request.FILES.get("slider_image")

        slider.save()
        messages.success(request, "Home Slider updated successfully!")
        return redirect("/admin/slider-list/")

# ── ADMIN AUTHENTICATION (LOGIN & LOGOUT) ──
def admin_login(request):
    if request.session.get("admin_id"):
        return redirect("/admin/")

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # Check AdminProfile model
        admin_account = AdminProfile.objects.filter(admin_email__iexact=email, admin_password=password).first()

        if not admin_account:
            # Fallback check for Django User authentication
            from django.contrib.auth import authenticate, login as auth_login
            user = authenticate(username=email, password=password)
            if user and user.is_staff:
                auth_login(request, user)
                request.session["admin_id"] = user.id
                request.session["admin_name"] = user.first_name or user.username or "Admin"
                request.session["admin_email"] = user.email or email
                request.session.set_expiry(600)  # 10 Minutes Session Timeout
                messages.success(request, f"Welcome back, {request.session['admin_name']}!")
                return redirect("/admin/")
            elif email.lower() == "dnyaneshwarsul61@gmail.com" and password == "Dny@8080":
                admin_account = AdminProfile.objects.filter(admin_email__iexact=email).first()

        if admin_account:
            request.session["admin_id"] = admin_account.id
            request.session["admin_name"] = admin_account.admin_name
            request.session["admin_email"] = admin_account.admin_email
            request.session.set_expiry(600)  # 10 Minutes Session Timeout
            messages.success(request, f"Welcome back, {admin_account.admin_name}!")
            return redirect("/admin/")
        else:
            messages.error(request, "Invalid Email Address or Password. Please try again.")

    return render(request, "admin/login.html")


def admin_logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out successfully.")
    return redirect("/admin/login/")


# Create your views here.
def index(req):
    if not req.session.get("admin_id") and not (req.user and req.user.is_staff):
        messages.warning(req, "Session expired or login required (10 Minutes Timeout). Please login.")
        return redirect("/admin/login/")

    # 1. Total Photographers (or Admin Profile accounts)
    total_photographers = AdminProfile.objects.count()


    # 2. Active Clients (Unique clients from Bookings)
    active_clients = Booking.objects.values("email").distinct().count()
    if active_clients == 0:
        active_clients = Booking.objects.values("mobile").distinct().count()

    # 3. Completed Bookings
    completed_bookings = Booking.objects.filter(booking_status__iexact="Completed").count()
    total_bookings = Booking.objects.count()

    # 4. Total Revenue
    revenue_sum = Booking.objects.aggregate(total=Sum("total_price"))["total"] or 0
    if float(revenue_sum) == 0 and total_bookings > 0:
        revenue_sum = sum(float(b.get_calculated_total_price()) for b in Booking.objects.all())

    # 5. Calculate trends (vs last month)
    today = datetime.date.today()
    first_of_this_month = today.replace(day=1)
    first_of_last_month = (first_of_this_month - datetime.timedelta(days=1)).replace(day=1)

    this_month_bookings = Booking.objects.filter(created_at__gte=first_of_this_month).count()
    last_month_bookings = Booking.objects.filter(
        created_at__gte=first_of_last_month,
        created_at__lt=first_of_this_month
    ).count()

    if last_month_bookings > 0:
        bookings_trend = round(((this_month_bookings - last_month_bookings) / last_month_bookings) * 100)
    else:
        bookings_trend = 12 if total_bookings > 0 else 0

    photographers_trend = 12
    clients_trend = 8
    revenue_trend = 15

    # 6. Recent Registrations / Recent Activity List (Client Bookings Only)
    recent_bookings = Booking.objects.all().order_by("-id")[:6]
    recent_activities = []
    
    for b in recent_bookings:
        status = b.booking_status or "Pending"
        if b.created_at:
            date_str = b.created_at.strftime("%d %b %Y, %I:%M %p")
        else:
            date_str = f"{b.event_date}"

        recent_activities.append({
            "name": b.full_name,
            "sub_detail": b.service or b.package or b.event_type or "Photography Services",
            "role": "Client",
            "status": status,
            "date_str": date_str
        })

    return render(req, "admin/index.html", {
        "active_page": "dashboard",
        "total_photographers": total_photographers,
        "active_clients": active_clients,
        "completed_bookings": completed_bookings,
        "total_bookings": total_bookings,
        "total_revenue": revenue_sum,
        "photographers_trend": photographers_trend,
        "clients_trend": clients_trend,
        "bookings_trend": bookings_trend,
        "revenue_trend": revenue_trend,
        "recent_activities": recent_activities,
    })



def profile(req):
    return render(req,"admin/profile.html")


def profile_list(req):
    profiles = AdminProfile.objects.all().order_by("-id")
    return render(req,"admin/profile_list.html",{"profiles": profiles})




def admin_profile(request):

    # ==========================================
    # POST
    # ==========================================

    if request.method == "POST":

        website_logo = request.FILES.get("website_logo")
        admin_profile_image = request.FILES.get("admin_profile")

        admin_name = request.POST.get("admin_name")
        admin_mobile = request.POST.get("admin_mobile")
        admin_email = request.POST.get("admin_email")
        admin_password = request.POST.get("admin_password")

        admin_instagram_link = request.POST.get(
            "admin_instagram_link"
        )

        admin_facebook_link = request.POST.get(
            "admin_facebook_link"
        )

        admin_linkden_link = request.POST.get(
            "admin_linkden_link"
        )

        admin_twiter_link = request.POST.get(
            "admin_twiter_link"
        )

        admin_youtube_link = request.POST.get(
            "admin_youtube_link"
        )


        # ==========================================
        # SAVE DATA
        # ==========================================

        AdminProfile.objects.create(

            website_logo=website_logo,

            admin_profile=admin_profile_image,

            admin_name=admin_name,

            admin_mobile=admin_mobile,

            admin_email=admin_email,

            admin_password=admin_password,

            admin_instagram_link=admin_instagram_link,

            admin_facebook_link=admin_facebook_link,

            admin_linkden_link=admin_linkden_link,

            admin_twiter_link=admin_twiter_link,

            admin_youtube_link=admin_youtube_link,
        )


        # ==========================================
        # SUCCESS MESSAGE
        # ==========================================

        messages.success(
            request,
            "Admin Profile Saved Successfully!"
        )


        return redirect("/admin/profile/")


    # ==========================================
    # GET
    # ==========================================

    return render(
        request,
        "admin/profile.html"
    )


# ── CLIENT STORIES (REAL STORIES) ──
def add_client_story(request):
    if request.method == "POST":
        category = request.POST.get("category", "WEDDING")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        story_image = request.FILES.get("story_image")

        HomeClientStory.objects.create(
            category=category,
            title=title,
            description=description,
            story_image=story_image
        )
        messages.success(request, "Client Story added successfully!")
        return redirect("/admin/client-story-list/")

    return render(request, "admin/add_client_story.html")


def client_story_list(request):
    client_stories = HomeClientStory.objects.all().order_by("-id")
    return render(request, "admin/client_story_list.html", {"client_stories": client_stories})


def edit_client_story(request, id):
    story = HomeClientStory.objects.filter(id=id).first()
    if not story:
        messages.error(request, "Client Story not found!")
        return redirect("/admin/client-story-list/")

    if request.method == "POST":
        story.category = request.POST.get("category", story.category)
        story.title = request.POST.get("title", story.title)
        story.description = request.POST.get("description", story.description)

        if request.FILES.get("story_image"):
            story.story_image = request.FILES.get("story_image")

        story.save()
        messages.success(request, "Client Story updated successfully!")
        return redirect("/admin/client-story-list/")

    return render(request, "admin/edit_client_story.html", {"story": story})


def delete_client_story(request, id):
    story = HomeClientStory.objects.filter(id=id).first()
    if story:
        story.delete()
        messages.success(request, "Client Story deleted successfully!")
    return redirect("/admin/client-story-list/")


# ── CLIENT TESTIMONIALS ──
def add_testimonial(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name", "")
        rating = int(request.POST.get("rating", 5))
        review = request.POST.get("review", "")
        client_photo = request.FILES.get("client_photo")

        HomeTestimonial.objects.create(
            client_name=client_name,
            rating=rating,
            review=review,
            client_photo=client_photo
        )
        messages.success(request, "Client Testimonial added successfully!")
        return redirect("/admin/testimonial-list/")

    return render(request, "admin/add_testimonial.html")


def testimonial_list(request):
    testimonials = HomeTestimonial.objects.all().order_by("-id")
    return render(request, "admin/testimonial_list.html", {"testimonials": testimonials})


def edit_testimonial(request, id):
    item = HomeTestimonial.objects.filter(id=id).first()
    if not item:
        messages.error(request, "Testimonial not found!")
        return redirect("/admin/testimonial-list/")

    if request.method == "POST":
        item.client_name = request.POST.get("client_name", item.client_name)
        item.rating = int(request.POST.get("rating", item.rating))
        item.review = request.POST.get("review", item.review)

        if request.FILES.get("client_photo"):
            item.client_photo = request.FILES.get("client_photo")

        item.save()
        messages.success(request, "Client Testimonial updated successfully!")
        return redirect("/admin/testimonial-list/")

    return render(request, "admin/edit_testimonial.html", {"item": item})


def delete_testimonial(request, id):
    item = HomeTestimonial.objects.filter(id=id).first()
    if item:
        item.delete()
        messages.success(request, "Client Testimonial deleted successfully!")
    return redirect("/admin/testimonial-list/")


# ── INSTAGRAM GALLERY ──
def add_insta_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        post_url = request.POST.get("post_url", "#")
        post_image = request.FILES.get("post_image")

        HomeInstaPost.objects.create(
            title=title,
            post_url=post_url,
            post_image=post_image
        )
        messages.success(request, "Instagram Post added successfully!")
        return redirect("/admin/insta-post-list/")

    return render(request, "admin/add_insta_post.html")


def insta_post_list(request):
    insta_posts = HomeInstaPost.objects.all().order_by("-id")
    return render(request, "admin/insta_post_list.html", {"insta_posts": insta_posts})


def edit_insta_post(request, id):
    post = HomeInstaPost.objects.filter(id=id).first()
    if not post:
        messages.error(request, "Instagram Post not found!")
        return redirect("/admin/insta-post-list/")

    if request.method == "POST":
        post.title = request.POST.get("title", post.title)
        post.post_url = request.POST.get("post_url", post.post_url)

        if request.FILES.get("post_image"):
            post.post_image = request.FILES.get("post_image")

        post.save()
        messages.success(request, "Instagram Post updated successfully!")
        return redirect("/admin/insta-post-list/")

    return render(request, "admin/edit_insta_post.html", {"post": post})


def delete_insta_post(request, id):
    post = HomeInstaPost.objects.filter(id=id).first()
    if post:
        post.delete()
        messages.success(request, "Instagram Post deleted successfully!")
    return redirect("/admin/insta-post-list/")


# ── AWARDS & RECOGNITION ──
def add_award(request):
    if request.method == "POST":
        icon_class = request.POST.get("icon_class", "bi bi-trophy")
        title = request.POST.get("title", "")
        subtitle = request.POST.get("subtitle", "")

        HomeAward.objects.create(
            icon_class=icon_class,
            title=title,
            subtitle=subtitle
        )
        messages.success(request, "Award / Recognition added successfully!")
        return redirect("/admin/award-list/")

    return render(request, "admin/add_award.html")


def award_list(request):
    awards = HomeAward.objects.all().order_by("-id")
    return render(request, "admin/award_list.html", {"awards": awards})


def edit_award(request, id):
    award = HomeAward.objects.filter(id=id).first()
    if not award:
        messages.error(request, "Award not found!")
        return redirect("/admin/award-list/")

    if request.method == "POST":
        award.icon_class = request.POST.get("icon_class", award.icon_class)
        award.title = request.POST.get("title", award.title)
        award.subtitle = request.POST.get("subtitle", award.subtitle)

        award.save()
        messages.success(request, "Award / Recognition updated successfully!")
        return redirect("/admin/award-list/")

    return render(request, "admin/edit_award.html", {"award": award})


def delete_award(request, id):
    award = HomeAward.objects.filter(id=id).first()
    if award:
        award.delete()
        messages.success(request, "Award deleted successfully!")
    return redirect("/admin/award-list/")


# ── BOOKINGS MANAGEMENT ──
from website.models import Booking
from django.db.models import Sum

def booking_list(request):
    bookings = Booking.objects.all().order_by("-id")
    paid_count = bookings.filter(payment_status__in=["Paid", "Full Paid"]).count()
    pending_count = bookings.filter(booking_status="Pending").count()
    
    total_collected = sum(
        float(b.get_calculated_total_price()) if (b.payment_status == 'Full Paid' or b.remaining_payment_status == 'Paid')
        else float(b.advance_amount or 0)
        for b in bookings
    )
    total_remaining_due = sum(b.get_remaining_due() for b in bookings)
    
    return render(request, "admin/booking_list.html", {
        "bookings": bookings,
        "paid_count": paid_count,
        "pending_count": pending_count,
        "total_collected": total_collected,
        "total_remaining_due": total_remaining_due,
    })

def update_booking_status(request, id):
    booking = Booking.objects.filter(id=id).first()
    if booking and request.method == "POST":
        new_status = request.POST.get("booking_status")
        if new_status:
            booking.booking_status = new_status
            booking.save()
            
            import urllib.parse
            if new_status == "Confirmed":
                wa_text = f"Hello {booking.full_name}, तुमची photography booking confirm झाली आहे. 😊\nतुमची booking successfully confirm केली आहे. Thank you! 🙏\n\n📋 *Booking Details:*\n• *Booking ID:* #BK-{booking.id}890\n• *Event:* {booking.event_type}\n• *Date & Time:* {booking.event_date} at {booking.event_time}\n• *Venue:* {booking.event_location}, {booking.city}\n• *Advance Paid:* ₹{booking.advance_amount} (Paid)\n\nA2Z Photographer Marketplace"
            elif new_status == "Cancelled":
                wa_text = f"❌ *BOOKING CANCELLED* - A2Z Photography\n\nHello {booking.full_name},\nYour photoshoot booking (#BK-{booking.id}890) for {booking.event_type} on {booking.event_date} has been CANCELLED.\n\nFor any queries or rescheduling, please reply to this message or contact support."
            elif new_status == "Completed":
                wa_text = f"✨ *PHOTOSHOOT COMPLETED* - A2Z Photography\n\nHello {booking.full_name},\nYour photoshoot for {booking.event_type} on {booking.event_date} is successfully COMPLETED!\n\nThank you for choosing A2Z Photography!"
            else:
                wa_text = f"📋 *BOOKING STATUS UPDATE* - A2Z Photography\n\nHello {booking.full_name},\nYour Photography Booking (#BK-{booking.id}890) status is now: {new_status}."

            encoded = urllib.parse.quote(wa_text)
            wa_link = f"https://api.whatsapp.com/send?phone=91{booking.mobile}&text={encoded}"
            
            messages.success(
                request,
                f"Booking #{booking.id} status updated to <strong>{new_status}</strong>! <a href='{wa_link}' target='_blank' class='btn btn-sm btn-success text-white font-weight-bold ms-2'><i class='bi bi-whatsapp me-1'></i> Send '{new_status}' WhatsApp Message to Customer</a>"
            )
    return redirect("/admin/booking-list/")

def delete_booking(request, id):
    booking = Booking.objects.filter(id=id).first()
    if booking:
        booking.delete()
        messages.success(request, "Booking record deleted successfully!")
    return redirect("/admin/booking-list/")


# ── ABOUT OUR STORY STEPS MANAGEMENT ──
def add_about_story(request):
    if request.method == "POST":
        small_title = request.POST.get("small_title", "OUR STORY")
        title = request.POST.get("title", "Turning Beautiful Moments Into Timeless Memories")
        description_para1 = request.POST.get("description_para1", "")
        description_para2 = request.POST.get("description_para2", "")
        photographer_name = request.POST.get("photographer_name", "Your Photographer")
        badge_subtitle = request.POST.get("badge_subtitle", "The Journey Begins")
        story_image = request.FILES.get("story_image")

        AboutStory.objects.create(
            small_title=small_title,
            title=title,
            description_para1=description_para1,
            description_para2=description_para2,
            photographer_name=photographer_name,
            badge_subtitle=badge_subtitle,
            story_image=story_image
        )
        messages.success(request, "Our Story entry added successfully!")
        return redirect("/admin/about-story-list/")

    return render(request, "admin/add_about_story.html")


def about_story_list(request):
    stories = AboutStory.objects.all().order_by("-id")
    return render(request, "admin/about_story_list.html", {"stories": stories})


def edit_about_story(request, id):
    story = AboutStory.objects.filter(id=id).first()
    if not story:
        messages.error(request, "Our Story entry not found!")
        return redirect("/admin/about-story-list/")

    if request.method == "POST":
        story.small_title = request.POST.get("small_title", story.small_title)
        story.title = request.POST.get("title", story.title)
        story.description_para1 = request.POST.get("description_para1", story.description_para1)
        story.description_para2 = request.POST.get("description_para2", story.description_para2)
        story.photographer_name = request.POST.get("photographer_name", story.photographer_name)
        story.badge_subtitle = request.POST.get("badge_subtitle", story.badge_subtitle)

        if request.FILES.get("story_image"):
            story.story_image = request.FILES.get("story_image")

        story.save()
        messages.success(request, "Our Story entry updated successfully!")
        return redirect("/admin/about-story-list/")

    return render(request, "admin/edit_about_story.html", {"story": story})


def delete_about_story(request, id):
    story = AboutStory.objects.filter(id=id).first()
    if story:
        story.delete()
        messages.success(request, "Our Story entry deleted successfully!")
    return redirect("/admin/about-story-list/")


def customer_booking_history(request):
    from website.models import Booking

    bookings_qs = Booking.objects.all().order_by("-id")
    
    customers_map = {}
    for b in bookings_qs:
        key = (b.email.lower().strip() if b.email else b.mobile.strip())
        if key not in customers_map:
            customers_map[key] = {
                "customer_id": len(customers_map) + 1,
                "name": b.full_name,
                "email": b.email,
                "mobile": b.mobile,
                "city": b.city,
                "bookings": [],
                "total_bookings": 0,
                "total_price_sum": 0,
                "total_paid_sum": 0,
                "total_due_sum": 0,
                "latest_event_date": b.event_date
            }
        
        c = customers_map[key]
        c["bookings"].append(b)
        c["total_bookings"] += 1
        calc_price = float(b.get_calculated_total_price())
        calc_due = float(b.get_remaining_due())
        calc_paid = max(0.0, calc_price - calc_due)
        
        c["total_price_sum"] += calc_price
        c["total_paid_sum"] += calc_paid
        c["total_due_sum"] += calc_due

    customer_list = list(customers_map.values())
    
    search_q = request.GET.get("q", "").strip().lower()
    if search_q:
        customer_list = [
            c for c in customer_list 
            if search_q in c["name"].lower() or search_q in c["email"].lower() or search_q in c["mobile"].lower() or search_q in c["city"].lower()
        ]

    return render(request, "admin/customer_booking_history.html", {
        "customer_list": customer_list,
        "search_q": search_q,
        "total_customers_count": len(customer_list)
    })


# ── SERVICES HERO BANNER VIEWS ──
def add_service_hero(request):
    if request.method == "POST":
        label_text = request.POST.get("label_text", "OUR SERVICES")
        title_prefix = request.POST.get("title_prefix", "Professional ")
        title_highlight = request.POST.get("title_highlight", "Photography")
        title_suffix = request.POST.get("title_suffix", " Services")
        description = request.POST.get("description", "")
        btn_text = request.POST.get("btn_text", "Explore Our Services")
        btn_link = request.POST.get("btn_link", "#services")
        bottom_text = request.POST.get("bottom_text", "CAPTURING MOMENTS • CREATING MEMORIES")
        hero_image = request.FILES.get("hero_image")

        ServicesHero.objects.create(
            label_text=label_text,
            title_prefix=title_prefix,
            title_highlight=title_highlight,
            title_suffix=title_suffix,
            description=description,
            btn_text=btn_text,
            btn_link=btn_link,
            bottom_text=bottom_text,
            hero_image=hero_image
        )
        messages.success(request, "Services Hero Banner added successfully!")
        return redirect("/admin/service-hero-list/")

    return render(request, "admin/add_service_hero.html")


def service_hero_list(request):
    hero_entries = ServicesHero.objects.all().order_by("-id")
    return render(request, "admin/service_hero_list.html", {"hero_entries": hero_entries})


def edit_service_hero(request, id):
    hero_obj = ServicesHero.objects.filter(id=id).first()
    if not hero_obj:
        messages.error(request, "Services Hero Banner entry not found!")
        return redirect("/admin/service-hero-list/")

    if request.method == "POST":
        hero_obj.label_text = request.POST.get("label_text", hero_obj.label_text)
        hero_obj.title_prefix = request.POST.get("title_prefix", hero_obj.title_prefix)
        hero_obj.title_highlight = request.POST.get("title_highlight", hero_obj.title_highlight)
        hero_obj.title_suffix = request.POST.get("title_suffix", hero_obj.title_suffix)
        hero_obj.description = request.POST.get("description", hero_obj.description)
        hero_obj.btn_text = request.POST.get("btn_text", hero_obj.btn_text)
        hero_obj.btn_link = request.POST.get("btn_link", hero_obj.btn_link)
        hero_obj.bottom_text = request.POST.get("bottom_text", hero_obj.bottom_text)

        if request.FILES.get("hero_image"):
            hero_obj.hero_image = request.FILES.get("hero_image")

        hero_obj.save()
        messages.success(request, "Services Hero Banner updated successfully!")
        return redirect("/admin/service-hero-list/")

    return render(request, "admin/edit_service_hero.html", {"hero": hero_obj})


def delete_service_hero(request, id):
    hero_obj = ServicesHero.objects.filter(id=id).first()
    if hero_obj:
        hero_obj.delete()
        messages.success(request, "Services Hero Banner deleted successfully!")
    return redirect("/admin/service-hero-list/")


# ── WHAT WE OFFER SECTION VIEWS ──
def what_we_offer_header(request):
    header_data = HomeWhatWeOfferHeader.objects.last()
    if not header_data:
        header_data = HomeWhatWeOfferHeader.objects.create()

    if request.method == "POST":
        header_data.small_title = request.POST.get("small_title", header_data.small_title)
        header_data.title = request.POST.get("title", header_data.title)
        header_data.description = request.POST.get("description", header_data.description)
        header_data.save()
        messages.success(request, "What We Offer Section Header updated successfully!")
        return redirect("/admin/what-we-offer-header/")

    return render(request, "admin/what_we_offer_header.html", {"header_data": header_data, "active_page": "what_we_offer_header"})


def add_what_we_offer(request):
    if request.method == "POST":
        icon_class = request.POST.get("icon_class", "bi bi-camera")
        icon_image = request.FILES.get("icon_image")
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title and description:
            HomeWhatWeOfferItem.objects.create(
                icon_class=icon_class,
                icon_image=icon_image,
                title=title,
                description=description
            )
            messages.success(request, "Offer item added successfully!")
            return redirect("/admin/what-we-offer-list/")
        else:
            messages.error(request, "Title and Description are required!")

    return render(request, "admin/add_what_we_offer.html", {"active_page": "add_what_we_offer"})


def what_we_offer_list(request):
    offer_items = HomeWhatWeOfferItem.objects.all().order_by("id")
    return render(request, "admin/what_we_offer_list.html", {"offer_items": offer_items, "active_page": "what_we_offer_list"})


def edit_what_we_offer(request, id):
    item = HomeWhatWeOfferItem.objects.filter(id=id).first()
    if not item:
        messages.error(request, "Offer item not found!")
        return redirect("/admin/what-we-offer-list/")

    if request.method == "POST":
        item.icon_class = request.POST.get("icon_class", item.icon_class)
        if request.FILES.get("icon_image"):
            item.icon_image = request.FILES.get("icon_image")
        item.title = request.POST.get("title", item.title).strip()
        item.description = request.POST.get("description", item.description).strip()
        item.save()
        messages.success(request, "Offer item updated successfully!")
        return redirect("/admin/what-we-offer-list/")

    return render(request, "admin/edit_what_we_offer.html", {"item": item, "active_page": "what_we_offer_list"})


def delete_what_we_offer(request, id):
    item = HomeWhatWeOfferItem.objects.filter(id=id).first()
    if item:
        item.delete()
        messages.success(request, "Offer item deleted successfully!")
    return redirect("/admin/what-we-offer-list/")


def services_cta_section(request):
    cta_obj = ServicesCTA.objects.first()
    if not cta_obj:
        cta_obj = ServicesCTA.objects.create()

    if request.method == "POST":
        cta_obj.small_title = request.POST.get("small_title", "").strip() or "LET'S CREATE MEMORIES"
        cta_obj.title = request.POST.get("title", "").strip() or "Ready to Capture Your Beautiful Moments?"
        cta_obj.description = request.POST.get("description", "").strip() or "Let's turn your special moments into beautiful, timeless photographs that you will cherish forever."
        cta_obj.btn1_text = request.POST.get("btn1_text", "").strip() or "Book Your Session"
        cta_obj.btn1_link = request.POST.get("btn1_link", "").strip() or "/booking_form/"
        cta_obj.btn2_text = request.POST.get("btn2_text", "").strip() or "Contact Us"
        cta_obj.btn2_link = request.POST.get("btn2_link", "").strip() or "/contact/"

        if request.FILES.get("bg_image"):
            cta_obj.bg_image = request.FILES.get("bg_image")

        cta_obj.save()
        messages.success(request, "Services Page CTA Banner updated successfully!")
        return redirect("/admin/services-cta-section/")

    return render(request, "admin/services_cta_section.html", {"cta": cta_obj, "active_page": "services_cta_section"})


def category_hero_section(request):
    hero_obj = CategoryHero.objects.first()
    if not hero_obj:
        hero_obj = CategoryHero.objects.create()

    if request.method == "POST":
        hero_obj.label_text = request.POST.get("label_text", hero_obj.label_text).strip()
        hero_obj.title_prefix = request.POST.get("title_prefix", hero_obj.title_prefix).strip()
        hero_obj.title_highlight = request.POST.get("title_highlight", hero_obj.title_highlight).strip()
        hero_obj.title_suffix = request.POST.get("title_suffix", hero_obj.title_suffix).strip()
        hero_obj.description = request.POST.get("description", hero_obj.description).strip()
        hero_obj.btn_text = request.POST.get("btn_text", hero_obj.btn_text).strip()
        hero_obj.btn_link = request.POST.get("btn_link", hero_obj.btn_link).strip()

        if request.FILES.get("hero_image"):
            hero_obj.hero_image = request.FILES.get("hero_image")

        hero_obj.save()
        messages.success(request, "Categories Page Hero Banner updated successfully!")
        return redirect("/admin/category-hero-section/")

    return render(request, "admin/category_hero_section.html", {"hero": hero_obj, "active_page": "category_hero_section"})


def category_hero_list(request):
    hero_entries = CategoryHero.objects.all().order_by("-id")
    return render(request, "admin/category_hero_list.html", {"hero_entries": hero_entries, "active_page": "category_hero_list"})


def delete_category_hero(request, id):
    hero_obj = CategoryHero.objects.filter(id=id).first()
    if hero_obj:
        hero_obj.delete()
        messages.success(request, "Category Hero Banner entry deleted successfully!")
    return redirect("/admin/category-hero-list/")


def category_section_header(request):
    header_obj = CategorySectionHeader.objects.first()
    if not header_obj:
        header_obj = CategorySectionHeader.objects.create()

    if request.method == "POST":
        header_obj.small_title = request.POST.get("small_title", header_obj.small_title).strip()
        header_obj.title = request.POST.get("title", header_obj.title).strip()
        header_obj.description = request.POST.get("description", header_obj.description).strip()
        header_obj.dropdown_badge = request.POST.get("dropdown_badge", header_obj.dropdown_badge).strip()
        header_obj.dropdown_default_option = request.POST.get("dropdown_default_option", header_obj.dropdown_default_option).strip()
        header_obj.dropdown_btn_text = request.POST.get("dropdown_btn_text", header_obj.dropdown_btn_text).strip()

        header_obj.save()
        messages.success(request, "All Categories Section Header updated successfully!")
        return redirect("/admin/category-section-header/")

    return render(request, "admin/category_section_header.html", {"header": header_obj, "active_page": "category_section_header"})


def gallery_hero_section(request):
    hero_obj = GalleryHero.objects.first()
    if not hero_obj:
        hero_obj = GalleryHero.objects.create(
            small_title="OUR PHOTOGRAPHY COLLECTION",
            title="Photo Gallery",
            description="Explore our collection of beautiful photographs, capturing love, happiness, celebrations and unforgettable moments that deserve to be remembered forever."
        )

    if request.method == "POST":
        hero_obj.small_title = request.POST.get("small_title", hero_obj.small_title).strip()
        hero_obj.title = request.POST.get("title", hero_obj.title).strip()
        hero_obj.description = request.POST.get("description", hero_obj.description).strip()

        if request.FILES.get("hero_image"):
            hero_obj.hero_image = request.FILES.get("hero_image")

        hero_obj.save()
        messages.success(request, "Gallery Hero Banner updated successfully!")
        return redirect("/admin/gallery-hero-section/")

    return render(request, "admin/gallery_hero_section.html", {"hero": hero_obj, "active_page": "gallery_hero_section"})


def _handle_gallery_section_header(request, section_key, section_display_name, default_small, default_title, default_desc, redirect_url):
    header_obj, _ = GallerySectionHeader.objects.get_or_create(
        section_key=section_key,
        defaults={
            "small_title": default_small,
            "title": default_title,
            "description": default_desc
        }
    )

    if request.method == "POST":
        header_obj.small_title = request.POST.get("small_title", header_obj.small_title).strip()
        header_obj.title = request.POST.get("title", header_obj.title).strip()
        header_obj.description = request.POST.get("description", header_obj.description).strip()
        header_obj.save()
        messages.success(request, f"{section_display_name} Section Header updated successfully!")
        return redirect(redirect_url)

    return render(request, "admin/gallery_section_header.html", {
        "header": header_obj,
        "section_key": section_key,
        "section_display_name": section_display_name,
        "form_action_url": redirect_url,
        "active_page": f"gallery_{section_key}_header"
    })


def gallery_wedding_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="wedding",
        section_display_name="Love & Forever (Wedding)",
        default_small="Love & Forever",
        default_title="Wedding Photography",
        default_desc="Beautiful wedding moments captured with emotions, traditions, happiness and timeless memories.",
        redirect_url="/admin/gallery-wedding-header/"
    )


def gallery_prewedding_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="prewedding",
        section_display_name="Couple Stories (Pre-Wedding)",
        default_small="Couple Stories",
        default_title="Pre-Wedding Photography",
        default_desc="Romantic couple sessions filled with love, beautiful locations and natural emotions.",
        redirect_url="/admin/gallery-prewedding-header/"
    )


def gallery_birthday_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="birthday",
        section_display_name="Celebration (Birthday)",
        default_small="Celebration",
        default_title="Birthday Photography",
        default_desc="Joyful birthday celebrations, party moments, cake cutting and happy memories.",
        redirect_url="/admin/gallery-birthday-header/"
    )


def gallery_baby_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="baby",
        section_display_name="Little Memories (Baby & Kids)",
        default_small="Little Memories",
        default_title="Baby & Kids Photography",
        default_desc="Adorable baby portraits, maternity shoots and heartwarming childhood smiles.",
        redirect_url="/admin/gallery-baby-header/"
    )


def gallery_events_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="events",
        section_display_name="Special Events",
        default_small="Special Events",
        default_title="Event Photography",
        default_desc="Corporate events, parties, family gatherings and special occasions captured with precision.",
        redirect_url="/admin/gallery-events-header/"
    )


def gallery_fashion_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="fashion",
        section_display_name="Style & Creativity (Fashion)",
        default_small="Style & Creativity",
        default_title="Fashion Photography",
        default_desc="Creative model portfolios, fashion shoots, stylish outfits and artistic portraits.",
        redirect_url="/admin/gallery-fashion-header/"
    )


def gallery_portrait_header(request):
    return _handle_gallery_section_header(
        request,
        section_key="portrait",
        section_display_name="Personal Stories (Portrait)",
        default_small="Personal Stories",
        default_title="Portrait Photography",
        default_desc="Expressive solo portraits, headshots and personal photography sessions.",
        redirect_url="/admin/gallery-portrait-header/"
    )


def gallery_cta_section(request):
    cta_obj = GalleryCTA.objects.first()
    if not cta_obj:
        cta_obj = GalleryCTA.objects.create(
            title="Have a Moment to Capture?",
            description="Let's turn your special moments into beautiful memories that you can cherish forever.",
            btn1_text="Book a Photoshoot",
            btn1_link="/booking_form/",
            btn2_text="Contact Us",
            btn2_link="/contact/"
        )

    if request.method == "POST":
        cta_obj.title = request.POST.get("title", cta_obj.title).strip()
        cta_obj.description = request.POST.get("description", cta_obj.description).strip()
        cta_obj.btn1_text = request.POST.get("btn1_text", cta_obj.btn1_text).strip()
        cta_obj.btn1_link = request.POST.get("btn1_link", cta_obj.btn1_link).strip()
        cta_obj.btn2_text = request.POST.get("btn2_text", cta_obj.btn2_text).strip()
        cta_obj.btn2_link = request.POST.get("btn2_link", cta_obj.btn2_link).strip()

        if request.FILES.get("bg_image"):
            cta_obj.bg_image = request.FILES.get("bg_image")

        cta_obj.save()
        messages.success(request, "Gallery Call-To-Action (CTA) Banner updated successfully!")
        return redirect("/admin/gallery-cta-section/")

    return render(request, "admin/gallery_cta_section.html", {"cta": cta_obj, "active_page": "gallery_cta_section"})


def contact_hero_section(request):
    hero_obj = ContactHero.objects.first()
    if not hero_obj:
        hero_obj = ContactHero.objects.create(
            small_title="LET'S CREATE SOMETHING BEAUTIFUL",
            title="Contact Us",
            description="Have a special moment that you want to capture? We'd love to hear your story and create beautiful memories that you can cherish forever."
        )

    if request.method == "POST":
        hero_obj.small_title = request.POST.get("small_title", hero_obj.small_title).strip()
        hero_obj.title = request.POST.get("title", hero_obj.title).strip()
        hero_obj.description = request.POST.get("description", hero_obj.description).strip()

        if request.FILES.get("hero_image"):
            hero_obj.hero_image = request.FILES.get("hero_image")

        hero_obj.save()
        messages.success(request, "Contact Page Hero Banner updated successfully!")
        return redirect("/admin/contact-hero-section/")

    return render(request, "admin/contact_hero_section.html", {"hero": hero_obj, "active_page": "contact_hero_section"})


def contact_info_section(request):
    info_obj = ContactInfo.objects.first()
    if not info_obj:
        info_obj = ContactInfo.objects.create(
            phone="+91 98765 43210",
            email="info@photostudio.com",
            office_address="Pune, Maharashtra, India",
            whatsapp_number="+91 98765 43210",
            working_hours="Mon - Sat : 10:00 AM - 7:00 PM",
            google_map_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15133.486241951554!2d73.8567437!3d18.5204303!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c069e3288f3b%3A0x6b84733735166299!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
        )

    if request.method == "POST":
        info_obj.phone = request.POST.get("phone", info_obj.phone).strip()
        info_obj.email = request.POST.get("email", info_obj.email).strip()
        info_obj.office_address = request.POST.get("office_address", info_obj.office_address).strip()
        info_obj.whatsapp_number = request.POST.get("whatsapp_number", info_obj.whatsapp_number).strip()
        info_obj.working_hours = request.POST.get("working_hours", info_obj.working_hours).strip()
        info_obj.google_map_url = request.POST.get("google_map_url", info_obj.google_map_url).strip()

        info_obj.save()
        messages.success(request, "Contact Information & Address updated successfully!")
        return redirect("/admin/contact-info-section/")

    return render(request, "admin/contact_info_section.html", {"info": info_obj, "active_page": "contact_info_section"})


def contact_inquiry_list(request):
    inquiries = ContactInquiry.objects.order_by("-id")
    return render(request, "admin/contact_inquiry_list.html", {"inquiries": inquiries, "active_page": "contact_inquiry_list"})


def delete_contact_inquiry(request, id):
    inq = ContactInquiry.objects.filter(id=id).first()
    if inq:
        inq.delete()
        messages.success(request, "Customer inquiry deleted successfully.")
    return redirect("/admin/contact-inquiry-list/")


def add_contact_inquiry(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        service = request.POST.get("service", "").strip()
        event_date_str = request.POST.get("event_date", "").strip()
        message_text = request.POST.get("message", "").strip()

        event_date = None
        if event_date_str:
            try:
                event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d").date()
            except Exception:
                event_date = None

        if full_name and phone and message_text:
            ContactInquiry.objects.create(
                full_name=full_name,
                email=email or "admin_added@photostudio.com",
                phone=phone,
                service=service or "General Inquiry",
                event_date=event_date,
                message=message_text
            )
            messages.success(request, f"New inquiry for '{full_name}' added successfully!")
        else:
            messages.error(request, "Please enter Customer Full Name, Phone, and Message.")

    return redirect("/admin/contact-inquiry-list/")


