import logging

import allure
from allure_commons.types import AttachmentType

logger = logging.getLogger(__name__)


def add_screenshot(driver):
    png = driver.get_screenshot_as_png()
    allure.attach(
        body=png, name="screenshot", attachment_type=AttachmentType.PNG, extension=".png"
    )


def add_logs(driver):
    try:
        # Стандартный метод Selenium для получения логов браузера
        browser_logs = driver.get_log("browser")
        if not browser_logs:
            return

        log = "".join(f"{entry['level']}: {entry['message']}\n" for entry in browser_logs)

        allure.attach(
            log,
            name="browser_logs",
            attachment_type=AttachmentType.TEXT,
            extension=".log",
        )
    except Exception as e:
        logger.warning(f"Не удалось собрать логи браузера: {e}")


def add_html(driver):
    html = driver.page_source
    allure.attach(
        body=html,
        name="page_source",
        attachment_type=AttachmentType.HTML,
        extension=".html",
    )


def add_video(driver):
    video_url = f"https://selenoid.autotests.cloud/video/{driver.session_id}.mp4"

    html = (
        "<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video></body></html>"
    )

    allure.attach(html, f"video_{driver.session_id}", AttachmentType.HTML, ".html")
