from django.db import models


class AdminProfile(models.Model):

    website_logo = models.ImageField(
        upload_to="admin/logo/",
        blank=True,
        null=True
    )

    admin_profile = models.ImageField(
        upload_to="admin/profile/",
        blank=True,
        null=True
    )

    admin_name = models.CharField(
        max_length=100
    )

    admin_mobile = models.CharField(
        max_length=10
    )

    admin_email = models.EmailField(
        max_length=150
    )

    admin_password = models.CharField(
        max_length=128
    )

    # Instagram
    admin_instagram_link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    # Facebook
    admin_facebook_link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    # LinkedIn
    admin_linkden_link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    # X / Twitter
    admin_twiter_link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    # YouTube
    admin_youtube_link = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.admin_name


class AccountSettings(models.Model):
    site_title = models.CharField(
        max_length=150,
        default="A2Z Photographer Marketplace"
    )
    support_email = models.EmailField(
        default="support@photographer.com"
    )
    support_phone = models.CharField(
        max_length=15,
        default="+91 9876543210"
    )
    currency = models.CharField(
        max_length=20,
        default="INR (₹)"
    )
    timezone = models.CharField(
        max_length=50,
        default="Asia/Kolkata"
    )
    enable_notifications = models.BooleanField(
        default=True
    )
    enable_maintenance_mode = models.BooleanField(
        default=False
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.site_title


class HomeSlider(models.Model):
    tagline = models.CharField(
        max_length=100,
        default="A2Z PHOTOGRAPHERS"
    )
    icon_class = models.CharField(
        max_length=50,
        default="bi bi-camera-fill"
    )
    title_line1 = models.CharField(
        max_length=100,
        default="Your Story."
    )
    title_line2_prefix = models.CharField(
        max_length=100,
        default="Our "
    )
    title_line2_highlight = models.CharField(
        max_length=100,
        default="Lens."
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    btn1_text = models.CharField(
        max_length=50,
        default="Find a Photographer"
    )
    btn1_link = models.CharField(
        max_length=255,
        default="#"
    )
    btn2_text = models.CharField(
        max_length=50,
        default="Explore Portfolio"
    )
    btn2_link = models.CharField(
        max_length=255,
        default="#"
    )
    slider_image = models.ImageField(
        upload_to="home/slider/"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.tagline} - {self.title_line1}"


class HomeAbout(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="About Me"
    )
    title = models.CharField(
        max_length=200,
        default="Turning Beautiful Moments Into Timeless Memories"
    )
    description_para1 = models.TextField(
        blank=True,
        null=True
    )
    description_para2 = models.TextField(
        blank=True,
        null=True
    )
    photographer_name = models.CharField(
        max_length=100,
        default="Your Photographer"
    )
    about_image = models.ImageField(
        upload_to="home/about/",
        blank=True,
        null=True
    )
    experience_years = models.CharField(
        max_length=50,
        default="10+"
    )
    experience_text = models.CharField(
        max_length=100,
        default="Years of Photography Experience"
    )
    feature1_title = models.CharField(
        max_length=100,
        default="Professional Photographers"
    )
    feature1_desc = models.CharField(
        max_length=255,
        default="Skilled photographers with creative experience and unique styles."
    )
    feature1_icon = models.CharField(
        max_length=50,
        default="bi bi-camera"
    )
    feature2_title = models.CharField(
        max_length=100,
        default="Creative Photography"
    )
    feature2_desc = models.CharField(
        max_length=255,
        default="Creative ideas that turn ordinary moments into beautiful memories."
    )
    feature2_icon = models.CharField(
        max_length=50,
        default="bi bi-stars"
    )
    feature3_title = models.CharField(
        max_length=100,
        default="Genuine Emotions"
    )
    feature3_desc = models.CharField(
        max_length=255,
        default="Natural emotions captured in authentic and meaningful frames."
    )
    feature3_icon = models.CharField(
        max_length=50,
        default="bi bi-heart"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class AboutPageInfo(models.Model):
    # Section 01: Hero Banner
    hero_label = models.CharField(
        max_length=100,
        default="ABOUT US"
    )
    hero_title = models.CharField(
        max_length=200,
        default="We Capture Moments. We Create Memories."
    )
    hero_description = models.TextField(
        blank=True,
        null=True,
        default="We are passionate about capturing genuine emotions, beautiful moments and meaningful stories that stay with you forever."
    )
    hero_image = models.ImageField(
        upload_to="about/hero/",
        blank=True,
        null=True
    )

    # Section 02: Who We Are / About Me
    small_title = models.CharField(
        max_length=100,
        default="ABOUT ME"
    )
    title = models.CharField(
        max_length=200,
        default="Turning Beautiful Moments Into Timeless Memories"
    )
    description_para1 = models.TextField(
        blank=True,
        null=True,
        default="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
    )
    description_para2 = models.TextField(
        blank=True,
        null=True,
        default="From weddings and pre-weddings to portraits, birthdays and special events, every photograph is created with creativity and attention to detail."
    )
    photographer_name = models.CharField(
        max_length=100,
        default="Your Photographer"
    )
    about_image = models.ImageField(
        upload_to="about/whoweare/",
        blank=True,
        null=True
    )

    experience_years = models.CharField(
        max_length=50,
        default="10+"
    )
    experience_text = models.CharField(
        max_length=100,
        default="Years of Photography Experience"
    )

    feature1_title = models.CharField(
        max_length=100,
        default="Professional Photographers"
    )
    feature1_desc = models.CharField(
        max_length=255,
        default="Skilled photographers with creative experience and unique styles."
    )
    feature1_icon = models.CharField(
        max_length=50,
        default="bi bi-camera"
    )

    feature2_title = models.CharField(
        max_length=100,
        default="Creative Photography"
    )
    feature2_desc = models.CharField(
        max_length=255,
        default="Creative ideas that turn ordinary moments into beautiful memories."
    )
    feature2_icon = models.CharField(
        max_length=50,
        default="bi bi-stars"
    )

    feature3_title = models.CharField(
        max_length=100,
        default="Genuine Emotions"
    )
    feature3_desc = models.CharField(
        max_length=255,
        default="Natural emotions captured in authentic and meaningful frames."
    )
    feature3_icon = models.CharField(
        max_length=50,
        default="bi bi-heart"
    )

    # Section 03: Our Story Header & Image Info
    story_small_title = models.CharField(
        max_length=100,
        default="OUR STORY"
    )
    story_title = models.CharField(
        max_length=200,
        default="Turning Beautiful Moments Into Timeless Memories"
    )
    story_desc1 = models.TextField(
        blank=True,
        null=True,
        default="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
    )
    story_desc2 = models.TextField(
        blank=True,
        null=True,
        default="From weddings and pre-weddings to portraits, birthdays and special events, every photograph is created with creativity and attention to detail."
    )
    story_image = models.ImageField(
        upload_to="about/story_header/",
        blank=True,
        null=True
    )
    story_badge_title = models.CharField(
        max_length=100,
        default="Your Photographer"
    )
    story_badge_subtitle = models.CharField(
        max_length=100,
        default="The Journey Begins"
    )

    # Section 04: What We Do Header Info
    what_we_do_label = models.CharField(
        max_length=100,
        default="WHAT WE DO"
    )
    what_we_do_title = models.CharField(
        max_length=200,
        default="Photography For Every Special Moment"
    )
    what_we_do_desc = models.TextField(
        blank=True,
        null=True,
        default="From intimate portraits to grand celebrations, we help you discover photography services that match your occasion and style."
    )

    # Section 05: Our Mission Header & Info
    mission_small_title = models.CharField(
        max_length=100,
        default="OUR MISSION"
    )
    mission_title = models.CharField(
        max_length=200,
        default="Capturing Emotion in Every Frame"
    )
    mission_quote = models.TextField(
        blank=True,
        null=True,
        default="Our mission is to connect people with passionate photographers who transform precious life events into timeless visual art."
    )
    mission_point1 = models.CharField(
        max_length=150,
        default="100% Quality Focused"
    )
    mission_point2 = models.CharField(
        max_length=150,
        default="Creative Excellence"
    )
    mission_point3 = models.CharField(
        max_length=150,
        default="Customer Satisfaction"
    )
    mission_bg_image = models.ImageField(
        upload_to="about/mission/",
        blank=True,
        null=True
    )

    # Section 06: Our Vision Header & Info
    vision_small_title = models.CharField(
        max_length=100,
        default="OUR VISION"
    )
    vision_title_line1 = models.CharField(
        max_length=100,
        default="Creating A Better"
    )
    vision_title_highlight = models.CharField(
        max_length=100,
        default="Photography Experience"
    )
    vision_description = models.TextField(
        blank=True,
        null=True,
        default="We envision a future where finding the perfect photographer is simple, transparent and inspiring."
    )
    vision_quote = models.TextField(
        blank=True,
        null=True,
        default="To become a trusted photography platform where every special moment finds the perfect photographer."
    )
    vision_image = models.ImageField(
        upload_to="about/vision/",
        blank=True,
        null=True
    )
    vision_val1 = models.CharField(
        max_length=100,
        default="Creative"
    )
    vision_val1_icon = models.CharField(
        max_length=50,
        default="bi bi-lightbulb"
    )
    vision_val2 = models.CharField(
        max_length=100,
        default="Professional"
    )
    vision_val2_icon = models.CharField(
        max_length=50,
        default="bi bi-award"
    )
    vision_val3 = models.CharField(
        max_length=100,
        default="Trusted"
    )
    vision_val3_icon = models.CharField(
        max_length=50,
        default="bi bi-shield-check"
    )
    vision_val4 = models.CharField(
        max_length=100,
        default="Accessible"
    )
    vision_val4_icon = models.CharField(
        max_length=50,
        default="bi bi-people"
    )

    # Section 08: Our Numbers Counter Stats Info
    numbers_small_title = models.CharField(
        max_length=100,
        default="OUR NUMBERS"
    )
    numbers_title = models.CharField(
        max_length=200,
        default="Growing Together Through Photography"
    )
    numbers_desc = models.TextField(
        blank=True,
        null=True,
        default="Our growing photography community continues to capture beautiful stories."
    )
    stat1_count = models.CharField(max_length=50, default="500+")
    stat1_title = models.CharField(max_length=100, default="Happy Clients")
    stat1_icon = models.CharField(max_length=50, default="bi bi-people")

    stat2_count = models.CharField(max_length=50, default="150+")
    stat2_title = models.CharField(max_length=100, default="Professional Photographers")
    stat2_icon = models.CharField(max_length=50, default="bi bi-camera")

    stat3_count = models.CharField(max_length=50, default="1000+")
    stat3_title = models.CharField(max_length=100, default="Events Captured")
    stat3_icon = models.CharField(max_length=50, default="bi bi-calendar-heart")

    stat4_count = models.CharField(max_length=50, default="25+")
    stat4_title = models.CharField(max_length=100, default="Photography Categories")
    stat4_icon = models.CharField(max_length=50, default="bi bi-grid")

    # Section 10: Start Your Story CTA Info
    cta_small_title = models.CharField(
        max_length=100,
        default="START YOUR STORY"
    )
    cta_title = models.CharField(
        max_length=200,
        default="Your Story Deserves To Be Captured."
    )
    cta_desc = models.TextField(
        blank=True,
        null=True,
        default="Whether it is your wedding, a special celebration, a family moment or a personal milestone — find the right photographer to capture it beautifully."
    )
    cta_btn1_text = models.CharField(max_length=50, default="Book a Photographer")
    cta_btn1_link = models.CharField(max_length=255, default="/booking_form/")
    cta_btn2_text = models.CharField(max_length=50, default="Explore Categories")
    cta_btn2_link = models.CharField(max_length=255, default="/category/")
    cta_bg_image = models.ImageField(upload_to="about/cta/", blank=True, null=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class HomeService(models.Model):
    icon_class = models.CharField(
        max_length=50,
        default="bi bi-heart"
    )
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    service_image = models.ImageField(
        upload_to="home/services/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class HomeFeaturedWork(models.Model):
    title = models.CharField(
        max_length=150
    )
    category_name = models.CharField(
        max_length=150
    )
    work_image = models.ImageField(
        upload_to="home/featured/"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class HomeCategory(models.Model):
    category_name = models.CharField(
        max_length=150
    )
    category_image = models.ImageField(
        upload_to="home/categories/"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    sub_services = models.TextField(
        blank=True,
        null=True,
        help_text="Comma-separated sub services e.g. Candid, Traditional, Outdoor"
    )
    detail_image = models.ImageField(
        upload_to="home/categories/detail/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.category_name


class HomeVideoStory(models.Model):
    category_tag = models.CharField(
        max_length=100
    )
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    video_file = models.FileField(
        upload_to="home/videos/",
        blank=True,
        null=True
    )
    video_url = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class HomeGallery(models.Model):
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    category_name = models.CharField(
        max_length=100,
        default="Wedding",
        blank=True,
        null=True
    )
    subtitle = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    gallery_image = models.ImageField(
        upload_to="home/gallery/"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title or f"Gallery Image {self.id}"


class GalleryHero(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="OUR PHOTOGRAPHY COLLECTION"
    )
    title = models.CharField(
        max_length=200,
        default="Photo Gallery"
    )
    description = models.TextField(
        default="Explore our collection of beautiful photographs, capturing love, happiness, celebrations and unforgettable moments that deserve to be remembered forever."
    )
    hero_image = models.ImageField(
        upload_to="gallery/hero/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"



class HomeWhyUsHeader(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="ABOUT ME"
    )
    title = models.CharField(
        max_length=200,
        default="Turning Beautiful Moments Into Timeless Memories"
    )
    description = models.TextField(
        blank=True,
        null=True,
        default="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
    )
    section_image = models.ImageField(
        upload_to="why_us/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"


class HomeWhyUs(models.Model):
    icon_class = models.CharField(
        max_length=100,
        default="bi bi-camera",
        blank=True,
        null=True
    )
    icon_image = models.ImageField(
        upload_to="why_us/items/",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=150
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title



class HomeProcessHeader(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="OUR PROCESS"
    )
    title = models.CharField(
        max_length=200,
        default="How We Work"
    )
    description = models.TextField(
        blank=True,
        null=True,
        default="From the first conversation to the final delivery, we make your photography experience simple and enjoyable."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"


class HomeProcess(models.Model):
    step_number = models.CharField(
        max_length=20,
        default="01"
    )
    icon_class = models.CharField(
        max_length=100,
        default="bi bi-chat-heart",
        blank=True,
        null=True
    )
    icon_image = models.ImageField(
        upload_to="home/process/",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.step_number} - {self.title}"



class HomeClientStory(models.Model):
    category = models.CharField(
        max_length=100,
        default="WEDDING"
    )
    title = models.CharField(
        max_length=150
    )
    description = models.TextField()
    story_image = models.ImageField(
        upload_to="home/client_stories/"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.category} - {self.title}"


class HomeTestimonial(models.Model):
    client_name = models.CharField(
        max_length=100
    )
    client_photo = models.ImageField(
        upload_to="home/testimonials/",
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        default=5
    )
    review = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.client_name} ({self.rating} Stars)"


class HomeInstaPost(models.Model):
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    post_image = models.ImageField(
        upload_to="home/instagram/"
    )
    post_url = models.URLField(
        max_length=500,
        default="#"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title or f"Insta Post {self.id}"


class HomeAward(models.Model):
    icon_class = models.CharField(
        max_length=50,
        default="bi bi-trophy"
    )
    title = models.CharField(
        max_length=150
    )
    subtitle = models.CharField(
        max_length=150
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} ({self.subtitle})"


class AboutStory(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="OUR STORY"
    )
    title = models.CharField(
        max_length=200,
        default="Turning Beautiful Moments Into Timeless Memories"
    )
    description_para1 = models.TextField(
        blank=True,
        null=True,
        default="I am a professional photographer passionate about capturing real emotions, natural expressions and beautiful stories."
    )
    description_para2 = models.TextField(
        blank=True,
        null=True,
        default="From weddings and pre-weddings to portraits, birthdays and special events, every photograph is created with creativity and attention to detail."
    )
    story_image = models.ImageField(
        upload_to="about/story/",
        blank=True,
        null=True
    )
    photographer_name = models.CharField(
        max_length=100,
        default="Your Photographer"
    )
    badge_subtitle = models.CharField(
        max_length=100,
        default="The Journey Begins"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class ServicesHero(models.Model):
    label_text = models.CharField(
        max_length=100,
        default="OUR SERVICES"
    )
    title_prefix = models.CharField(
        max_length=100,
        default="Professional "
    )
    title_highlight = models.CharField(
        max_length=100,
        default="Photography"
    )
    title_suffix = models.CharField(
        max_length=100,
        default=" Services"
    )
    description = models.TextField(
        default="We capture your most beautiful moments with creativity, emotion and timeless photography. From weddings and portraits to birthdays, baby shoots and special events."
    )
    btn_text = models.CharField(
        max_length=100,
        default="Explore Our Services"
    )
    btn_link = models.CharField(
        max_length=255,
        default="#services"
    )
    bottom_text = models.CharField(
        max_length=200,
        default="CAPTURING MOMENTS • CREATING MEMORIES"
    )
    hero_image = models.ImageField(
        upload_to="services/hero/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.label_text} - {self.title_prefix}{self.title_highlight}{self.title_suffix}"


class HomeWhatWeOfferHeader(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="WHAT WE OFFER"
    )
    title = models.CharField(
        max_length=200,
        default="More Than Just Photography"
    )
    description = models.TextField(
        blank=True,
        null=True,
        default="We provide complete photography solutions to make your special moments beautiful, memorable and timeless."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"


class HomeWhatWeOfferItem(models.Model):
    icon_class = models.CharField(
        max_length=100,
        default="bi bi-camera",
        blank=True,
        null=True
    )
    icon_image = models.ImageField(
        upload_to="home/offer/",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=150
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class CategoryHero(models.Model):
    label_text = models.CharField(
        max_length=100,
        default="Photography Categories"
    )
    title_prefix = models.CharField(
        max_length=100,
        default="Explore Our "
    )
    title_highlight = models.CharField(
        max_length=100,
        default="Photography"
    )
    title_suffix = models.CharField(
        max_length=100,
        default=" Categories"
    )
    description = models.TextField(
        default="Discover professional photography services for every special moment, occasion and beautiful story you want to preserve forever."
    )
    btn_text = models.CharField(
        max_length=100,
        default="Explore Categories"
    )
    btn_link = models.CharField(
        max_length=255,
        default="#all-categories"
    )
    hero_image = models.ImageField(
        upload_to="categories/hero/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.label_text} - {self.title_prefix}{self.title_highlight}{self.title_suffix}"


class ServicesCTA(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="LET'S CREATE MEMORIES"
    )
    title = models.CharField(
        max_length=200,
        default="Ready to Capture Your Beautiful Moments?"
    )
    description = models.TextField(
        default="Let's turn your special moments into beautiful, timeless photographs that you will cherish forever."
    )
    btn1_text = models.CharField(
        max_length=50,
        default="Book Your Session"
    )
    btn1_link = models.CharField(
        max_length=255,
        default="/booking_form/"
    )
    btn2_text = models.CharField(
        max_length=50,
        default="Contact Us"
    )
    btn2_link = models.CharField(
        max_length=255,
        default="/contact/"
    )
    bg_image = models.ImageField(
        upload_to="services/cta/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"


class CategorySectionHeader(models.Model):
    small_title = models.CharField(
        max_length=100,
        default="BROWSE CATEGORIES"
    )
    title = models.CharField(
        max_length=200,
        default="All Photography Categories"
    )
    description = models.TextField(
        default="Choose the photography style that matches your occasion and discover the perfect photographer for your needs."
    )
    dropdown_badge = models.CharField(
        max_length=100,
        default="QUICK FILTER CATEGORY DROPDOWN"
    )
    dropdown_default_option = models.CharField(
        max_length=150,
        default="✨ Show All Photography Categories"
    )
    dropdown_btn_text = models.CharField(
        max_length=100,
        default="Book Category"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.small_title} - {self.title}"


class GallerySectionHeader(models.Model):
    section_key = models.CharField(
        max_length=50,
        unique=True
    )
    small_title = models.CharField(
        max_length=100,
        default="Love & Forever"
    )
    title = models.CharField(
        max_length=200,
        default="Wedding Photography"
    )
    description = models.TextField(
        default="Beautiful wedding moments captured with emotions, traditions, happiness and timeless memories."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.section_key} - {self.title}"


class GalleryCTA(models.Model):
    title = models.CharField(
        max_length=200,
        default="Have a Moment to Capture?"
    )
    description = models.TextField(
        default="Let's turn your special moments into beautiful memories that you can cherish forever."
    )
    btn1_text = models.CharField(
        max_length=50,
        default="Book a Photoshoot"
    )
    btn1_link = models.CharField(
        max_length=255,
        default="/booking_form/"
    )
    btn2_text = models.CharField(
        max_length=50,
        default="Contact Us"
    )
    btn2_link = models.CharField(
        max_length=255,
        default="/contact/"
    )
    bg_image = models.ImageField(
        upload_to="gallery/cta/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class ContactHero(models.Model):
    small_title = models.CharField(
        max_length=150,
        default="LET'S CREATE SOMETHING BEAUTIFUL"
    )
    title = models.CharField(
        max_length=200,
        default="Contact Us"
    )
    description = models.TextField(
        default="Have a special moment that you want to capture? We'd love to hear your story and create beautiful memories that you can cherish forever."
    )
    hero_image = models.ImageField(
        upload_to="contact/hero/",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    phone = models.CharField(
        max_length=30,
        default="+91 98765 43210"
    )
    email = models.EmailField(
        max_length=150,
        default="info@photostudio.com"
    )
    office_address = models.CharField(
        max_length=255,
        default="Pune, Maharashtra, India"
    )
    whatsapp_number = models.CharField(
        max_length=30,
        default="+91 98765 43210"
    )
    working_hours = models.CharField(
        max_length=100,
        default="Mon - Sat : 10:00 AM - 7:00 PM"
    )
    google_map_url = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15133.486241951554!2d73.8567437!3d18.5204303!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c069e3288f3b%3A0x6b84733735166299!2sPune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.phone} - {self.email}"







