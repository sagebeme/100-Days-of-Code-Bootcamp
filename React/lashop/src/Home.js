import React from "react";
import "./Home.css";
import Product from "./Product";

function Home() {
    return(
        <div className="home">
            <div className="home__container">
                <img src="https://www.x-cart.com/wp-content/uploads/2019/01/ecommerce-768x278.jpg" alt="Home" className="home__image"/>

                <div className="home__row">
                    <Product
                        id="12321341"
                        title="Bennett Mystic 15.6 inch Laptop Shoulder Messenger Sling Office Bag, Water Repellent Fabric for Men and Women (Blue)"
                        price={11.96}
                        rating={5}
                        image="https://images-na.ssl-images-amazon.com/images/I/71mEsHyzSCL._SL1000_.jpg"
                    />
                    <Product
                        id="49538094"
                        title="IFB 30 L Convection Microwave Oven (30BRC2, Black, With Starter Kit)"
                        price={239.0}
                        rating={4}
                        image="https://images-na.ssl-images-amazon.com/images/I/81D8pNFmWzL._SL1500_.jpg"
                    />
                </div>

                <div className="home__row">
                    <Product/>
                    <Product/>
                </div>

                <div className="home__row">
                    <Product/>
                    <Product/>
                </div>
            </div>
        </div>
    )
}

export default Home