data_examples = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "slug": {"type": "string"},
                    "image": {"type": "string"},
                    "seo_description": {"type": "string"},
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "slug": {"type": "string"},
                                "date_create": {"type": "string"},
                                "title": {"type": "string"},
                                "link": {"type": "string"},
                            },
                            "required": ["name", "slug", "date_create", "title", "link"],
                        },
                    },
                    "og_title": {"type": "string"},
                    "og_description": {"type": "string"},
                    "og_image": {"type": "string"},
                    "site_type": {
                        "oneOf": [
                            {"type": "boolean"},
                            {"type": "array", "items": {"type": "string"}},
                        ]
                    },
                    "technology": {
                        "oneOf": [
                            {"type": "boolean"},
                            {"type": "array", "items": {"type": "string"}},
                        ]
                    },
                    "direction": {"type": "string"},
                },
                "required": ["name", "slug", "image", "seo_description", "tags"],
            },
        },
        "meta": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "count": {"type": "integer"},
            },
            "required": ["limit", "offset", "count"],
        },
    },
    "required": ["data", "meta"],
}
