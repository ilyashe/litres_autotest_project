post_auth_successful = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "additionalProperties": False,
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "sid": {
              "type": "string"
            }
          },
          "required": [
            "sid"
          ]
        }
      },
      "required": [
        "data"
      ]
    }
  },
  "required": [
    "status",
    "error",
    "payload"
  ]
}

post_auth_unsuccessful = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "title"
      ]
    }
  },
  "required": [
    "status",
    "error"
  ]
}

