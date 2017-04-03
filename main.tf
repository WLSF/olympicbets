# Configuration to Heroku provider

# Setup 1 application or manage it if already exists.
provider "heroku" {
    email = "${var.heroku_email}"
    api_key = "${var.heroku_key}"
}   

resource "heroku_app" "default" {
    name    = "${var.heroku_app}"
    region  = "${var.heroku_region}"
}

resource "heroku_addon" "database" {
    app = "${var.heroku_app}"
    plan = "heroku-postgresql:hobby-dev"
}

resource "heroku_addon" "deployment" {
    app = "${var.heroku_app}"
    plan = "codeship:free"
}