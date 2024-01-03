const canvas = document.querySelector("canvas")

const cntx = canvas.getContext('2d')

canvas.width = innerWidth
canvas.height = innerHeight

class Player{
    constructor(x, y, radius, color){
        this.x =x
        this.y =y
        this.radius = radius
        this.color = color
    }

    drawPlayer() {
        cntx.beginPath()
        cntx.arc(this.x, this.y, this.
            radius,0, Math.PI * 2, false)
        cntx.fillStyle =  this.color
        cntx.fill()
    }
}

class Projectile{
    constructor(x, y, radius, color, velocity){
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
        this.velocity = velocity
    }

    drawProjectile() {
        cntx.beginPath()
        cntx.arc(this.x, this.y, this.
            radius,0, Math.PI * 2, false)
        cntx.fillStyle =  this.color
        cntx.fill()
    }

    update(){
        this.drawProjectile()
        this.x = this.x +this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

class Enemy{
    constructor(x, y, radius, color, velocity){
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color
        this.velocity = velocity
    }

    drawProjectile() {
        cntx.beginPath()
        cntx.arc(this.x, this.y, this.
            radius,0, Math.PI * 2, false)
        cntx.fillStyle =  this.color
        cntx.fill()
    }

    update(){
        this.drawProjectile()
        this.x = this.x +this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

const x = canvas.width / 2
const y = canvas.height / 2

const player = new Player(x, y, 30, 'blue')

const projectiles = []
const enemies = []


function spawnEnemies() {
    setInterval(() => {
        const x = 100
        const y = 100
        const radius = 30
        const color = 'green'
        const velocity = {
            x: 1,
            y: 1
        }
        enemies.push (new Enemy(x, y, radius, color,
            velocity))

    }, 1000);
}


function animate() {
    requestAnimationFrame(animate)
    cntx.clearRect(0, 0, canvas.width, canvas.height)
    player.drawPlayer()
    projectiles.forEach(projectile =>
        {
        projectile.update()
    });

    enemies.forEach(enemy => (
        enemy.update()
    ))
}

addEventListener('click', (event)=>{

    const angle = Math.atan2(
        event.clientY - canvas.height / 2,
        event.clientX - canvas.width / 2
        )

    const velocity = {
        x: Math.cos(angle),
        y: Math.sin(angle)
    }

    projectiles.push(new Projectile(
        canvas.width / 2,
        canvas.height/ 2,
        5, 'pink', velocity)
    )
})

animate()
spawnEnemies()