// Selecting the canvas element from the HTML document
const canvas = document.querySelector('canvas');

// Getting the 2D rendering context of the canvas
const c = canvas.getContext('2d');

// Setting the width and height of the canvas to match the window size
canvas.width = innerWidth;
canvas.height = innerHeight;

// Defining the Player class
class Player {
    // Constructor for initializing player properties
    constructor() {
        // Setting initial position of the player
        this.position = {
            x: 200,
            y: 200
        };

        // Setting initial velocity of the player
        this.velocity = {
            x: 0,
            y: 0
        };

        // Creating an image object for the player's spaceship
        const image = new Image();
        // Setting the source of the image
        image.src = './img/spaceship.png'; // Adjust the path and filename as needed
        // Assigning the image object to the player
        this.image = image;

        // Setting the width and height of the player
        this.width = 100;
        this.height = 100;
    }

    // Method to draw the player on the canvas
    draw() {
        // Drawing the player's image on the canvas at the specified position
        c.drawImage(this.image, this.position.x, this.position.y);
    }
}

// Creating a new instance of the Player class
const player = new Player();

// Drawing the player on the canvas
player.draw();

// Function to animate the canvas
function animate() {
    // Requesting the next animation frame
    requestAnimationFrame(animate);
    // Logging a message to the console for testing
    console.log('Animation running...');
}

// Starting the animation loop
animate();
