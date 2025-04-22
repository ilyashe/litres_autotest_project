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
  "additionalProperties": False,
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

put_add_book_to_basket_successful = {
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
            "added_art_ids": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                }
              ]
            },
            "failed_art_ids": {
              "type": "array",
              "items": {}
            }
          },
          "required": [
            "added_art_ids",
            "failed_art_ids"
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

put_add_book_to_basket_validation_error ={
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
        },
        "detail": {
          "type": "string"
        },
        "error_descriptions": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "loc": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string"
                    },
                    {
                      "type": "string"
                    },
                    {
                      "type": "string"
                    }
                  ]
                },
                "msg": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                }
              },
              "required": [
                "loc",
                "msg",
                "type"
              ]
            }
          ]
        }
      },
      "required": [
        "type",
        "title",
        "detail",
        "error_descriptions"
      ]
    }
  },
  "required": [
    "status",
    "error"
  ]
}

get_basket_status = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "error": {
            "type": "null"
        },
        "payload": {
            "properties": {
                "data": {
                    "properties": {
                        "account_money": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "accrued_bonuses": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "arts_in_cart": {
                            "items": {
                                "type": "integer"
                            },
                            "type": "array"
                        },
                        "base_cost": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "best_offer": {
                            "type": "string"
                        },
                        "bonus_money": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "can_be_paid_by_account_money": {
                            "type": "boolean"
                        },
                        "can_earned_bonuses_amount_after_sign_up_loyalty": {
                            "type": ["null", "number"]
                        },
                        "count": {
                            "type": "integer"
                        },
                        "discount": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "earned_bonuses_amount": {
                            "type": "null"
                        },
                        "final_cost": {
                            "properties": {
                                "amount": {
                                    "type": "number"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ],
                            "type": "object"
                        },
                        "price_with_bonus": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "count",
                        "discount",
                        "bonus_money",
                        "account_money",
                        "best_offer",
                        "accrued_bonuses",
                        "final_cost",
                        "base_cost",
                        "can_be_paid_by_account_money",
                        "arts_in_cart",
                        "price_with_bonus",
                        "earned_bonuses_amount",
                        "can_earned_bonuses_amount_after_sign_up_loyalty"
                    ],
                    "type": "object"
                }
            },
            "required": [
                "data"
            ],
            "type": "object"
        },
        "status": {
            "type": "integer"
        }
    },
    "required": [
        "status",
        "error",
        "payload"
    ]
}

