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

        // Setting initial velocity of the player
        this.velocity = {
            x: 0,
            y: 0
        };

        // Creating an image object for the player's spaceship
        const image = new Image();
        // Setting the source of the image
        image.src = './img/spaceship.png';
        //listening to see when the image is fully loaded
        image.onload = ()=>{

            // Assigning the image object to the player
            this.image = image;

            //scaling the image to look smaller than it's original size
            const scale = .15

            // Setting the width and height of the player

            this.width = image.width * scale;
            this.height = image.height * scale;

            // Setting initial position of the player
            // moved it here because it was getting the width that was loading
            this.position = {
                x: canvas.width/2 - this.width/2,
                y: canvas.height - this.height - 20
            };
        }
    }

    // Method to draw the player on the canvas
    draw() {
        // c.fillStyle = 'red'
        // c.fillRect(this.position.x, this.position.y, this.position.width, this.position.height)
        // Drawing the player's image on the canvas at the specified position
        if (this.image)
        c.drawImage(
            this.image,
            this.position.x,
            this.position.y,
            this.width,
            this.height
        );
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
    c.fillStyle = 'black'
    c.fillRect(0,0, canvas.width, canvas.height)
    player.draw()
}

// Starting the animation loop
animate();

addEventListener('keydown',
({key})=>{//obj destructuring getting the key that's getting pressed
    switch(key){
        case 'a':
            console.log('left')
            break
        case 'd':
            console.log('right')
            break
        case ' ':
            console.log('space')
            break
        case 's':
            console.log('down')
            break
        case 'w':
            console.log('up')
            break
    }
})