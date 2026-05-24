from flask import Flask

website = Flask(__name__)

# =========================
# HOME PAGE
# =========================

@website.route("/")
def home():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Property Management System</title>

        <style>

            body{
                margin:0;
                font-family:Arial;
                background:#f4f6f9;
            }

            .navbar{
                background:#2c3e50;
                padding:20px;
                color:white;
                display:flex;
                justify-content:space-between;
                align-items:center;
            }

            .logo{
                font-size:30px;
                font-weight:bold;
            }

            .menu a{
                color:white;
                text-decoration:none;
                margin-left:20px;
                font-size:18px;
            }

            .hero{
                text-align:center;
                padding:60px;
            }

            .hero h1{
                font-size:55px;
                color:#2c3e50;
            }

            .hero p{
                font-size:24px;
                color:gray;
            }

            .btn{
                background:#3498db;
                color:white;
                padding:15px 30px;
                text-decoration:none;
                border-radius:10px;
                font-size:20px;
            }

            .properties{
                display:flex;
                justify-content:center;
                gap:30px;
                flex-wrap:wrap;
                padding:40px;
            }

            .card{
                background:white;
                width:300px;
                padding:20px;
                border-radius:15px;
                box-shadow:0px 0px 10px rgba(0,0,0,0.1);
            }

            .card img{
                width:100%;
                border-radius:10px;
            }

            .card h2{
                color:#2c3e50;
            }

            .price{
                color:green;
                font-size:24px;
                font-weight:bold;
            }

        </style>

    </head>

    <body>

        <div class="navbar">

            <div class="logo">🏠 PropertyHub</div>

            <div class="menu">

                <a href="/">Home</a>

                <a href="/properties">Properties</a>

                <a href="#">Login</a>

                <a href="#">Contact</a>

            </div>

        </div>

        <div class="hero">

            <h1>Find Your Dream Property 🚀</h1>

            <p>Professional Real Estate Website By Bhavesh</p>

            <br>

            <a href="/properties" class="btn">

                View Properties

            </a>

        </div>

        <div class="properties">

            <div class="card">

                <img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994">

                <h2>Luxury Villa</h2>

                <p>Mumbai</p>

                <p class="price">₹75,00,000</p>

            </div>

            <div class="card">

                <img src="https://images.unsplash.com/photo-1570129477492-45c003edd2be">

                <h2>Modern Apartment</h2>

                <p>Bangalore</p>

                <p class="price">₹45,00,000</p>

            </div>

            <div class="card">

                <img src="https://images.unsplash.com/photo-1600585154526-990dced4db0d">

                <h2>3BHK Flat</h2>

                <p>Pune</p>

                <p class="price">₹35,00,000</p>

            </div>

        </div>

    </body>

    </html>

    """

# =========================
# PROPERTIES PAGE
# =========================

@website.route("/properties")
def properties():

    return """

    <!DOCTYPE html>

    <html>

    <head>

        <title>Available Properties</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f6f9;
                padding:40px;
            }

            h1{
                text-align:center;
                color:#2c3e50;
            }

            .property-box{
                background:white;
                padding:20px;
                margin:20px auto;
                width:60%;
                border-radius:10px;
                box-shadow:0px 0px 10px rgba(0,0,0,0.1);
            }

            .price{
                color:green;
                font-size:22px;
                font-weight:bold;
            }

            .btn{
                background:#3498db;
                color:white;
                padding:10px 20px;
                text-decoration:none;
                border-radius:8px;
            }

        </style>

    </head>

    <body>

        <h1>🏠 Available Properties</h1>

        <div class="property-box">

            <h2>Luxury Villa</h2>

            <p>Location: Mumbai</p>

            <p class="price">₹75,00,000</p>

            <a href="/" class="btn">Back Home</a>

        </div>

        <div class="property-box">

            <h2>Modern Apartment</h2>

            <p>Location: Bangalore</p>

            <p class="price">₹45,00,000</p>

            <a href="/" class="btn">Back Home</a>

        </div>

        <div class="property-box">

            <h2>3BHK Flat</h2>

            <p>Location: Pune</p>

            <p class="price">₹35,00,000</p>

            <a href="/" class="btn">Back Home</a>

        </div>

    </body>

    </html>

    """

# =========================
# RUN WEBSITE
# =========================

if __name__ == "__main__":

    website.run(debug=false)