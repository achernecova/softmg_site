import json
import logging

logger = logging.getLogger(__name__)


class TransformAndGetData:

    @staticmethod
    def transformation_json(value):
        body = json.loads(value.content)
        logger.info(
            f"Трансформированный json ответ: {json.dumps(value.json(), indent=4, ensure_ascii=False)}"
        )
        return body

    @staticmethod
    def get_error_title(response):
        error_title = response["errors"][0]["title"]
        logger.info(f"Error: {error_title}")
        return error_title

    @staticmethod
    def get_count_data(response):
        body = json.loads(response.content)
        response_title = body["data"]
        return len(response_title)

    @staticmethod
    def get_meta_count(response):
        body = json.loads(response.content)
        response_meta = body["meta"]["count"]
        return response_meta

    def get_name_data(self, response):
        body = self.transformation_json(response)
        response_title = body["data"]
        names = [project.get("name", "") for project in response_title]
        return names


get_data_error = TransformAndGetData()
