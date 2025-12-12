from softmg_site.pages import B2BPageSelene
from softmg_site.pages import CodeigniterPageSelene
from softmg_site.pages import CustomSoftwarePageSelene
from softmg_site.pages import D2CPageSelene
from softmg_site.pages import EComPageSelene
from softmg_site.pages import FrameworkPageSelene
from softmg_site.pages import LandingPageSelene
from softmg_site.pages.main_page_selene import MainPageSelene
from softmg_site.pages import MobilePageSelene
from softmg_site.pages import OutstaffPageSelene
from softmg_site.pages import ProjectEuroVPNSelene
from softmg_site.pages import ProjectFindABuilderSelene
from softmg_site.pages import ProjectMintLinkSelene
from softmg_site.pages import ProjectSLSSelene
from softmg_site.pages import ProjectTradingPlatformSelene
from softmg_site.pages import ProjectVeganHotelSelene
from softmg_site.pages import PythonPageSelene
from softmg_site.pages import ReactPageSelene
from softmg_site.pages import SAASPageSelene
from softmg_site.pages import ServicesPageSelene
from softmg_site.pages import TechSupportPageSelene
from softmg_site.pages import SymfonyPageSelene
from softmg_site.pages import WebDevelopmentPageSelene


def get_page_instance_selene(page_name):
    page_classes = {
        "base_page": MainPageSelene,
        "services_page": ServicesPageSelene,
        "mobile_page": MobilePageSelene,
        "custom_software_dev_page": CustomSoftwarePageSelene,
        "outstaff_page": OutstaffPageSelene,
        "python": PythonPageSelene,
        #
        # "c_sharp_page": JavaPage,
        # "java": JavaPage,
        # "unity_page": JavaPage,
        # "golang_page": JavaPage,
        #
        "web_development_page": WebDevelopmentPageSelene,
        "e_com_page": EComPageSelene,
        # "cms": CMSPage,
        "landing": LandingPageSelene,
        "framework_page": FrameworkPageSelene,
        "b2b_page": B2BPageSelene,
        "d2c": D2CPageSelene,
        "saas": SAASPageSelene,
        "website_design_page": WebDevelopmentPageSelene,
        "tech_support_page": TechSupportPageSelene,
        # "wordpress": WordpressPage,
        # "joomla": JoomlaPage,
        # "opencart": OpencartPage,
        "reactjs": ReactPageSelene,
        # "laravel": LaravelPage,
        "symfony": SymfonyPageSelene,
        "codeigniter": CodeigniterPageSelene,
        # "project_page": ProjectPage,
        # "reviews": ReviewsPage,
        # "contacts": ContactPage,
        # "about": AboutPage,
        # # "blog": BlogPage,
        "project_euro_vpn": ProjectEuroVPNSelene,
        "project_find_a_builder": ProjectFindABuilderSelene,
        "project_mint_link": ProjectMintLinkSelene,
        "project_sls": ProjectSLSSelene,
        "project_vegan_hotel": ProjectVeganHotelSelene,
        "project_trading_platform": ProjectTradingPlatformSelene,
    }
    try:
        return page_classes[page_name]()
    except KeyError:
        raise ValueError(f"Неизвестная страница: {page_name}")
