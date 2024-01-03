const canvas = document.querySelector('canvas');

const cntx = canvas.getContext('2d');

canvas.width = innerWidth;
canvas.height = innerHeight;

class Player {
  constructor (x, y, radius, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
  }

  drawPlayer () {
    cntx.beginPath();
    cntx.arc(this.x, this.y, this
      .radius, 0, Math.PI * 2, false);
    cntx.fillStyle = this.color;
    cntx.fill();
  }
}

class Projectile {
  constructor (x, y, radius, color, velocity) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.velocity = velocity;
  }

  drawProjectile () {
    cntx.beginPath();
    cntx.arc(this.x, this.y, this
      .radius, 0, Math.PI * 2, false);
    cntx.fillStyle = this.color;
    cntx.fill();
  }

  update () {
    this.drawProjectile();
    this.x = this.x + this.velocity.x;
    this.y = this.y + this.velocity.y;
  }
}

class Enemy {
  constructor (x, y, radius, color, velocity) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.velocity = velocity;
  }

  drawProjectile () {
    cntx.beginPath();
    cntx.arc(this.x, this.y, this
      .radius, 0, Math.PI * 2, false);
    cntx.fillStyle = this.color;
    cntx.fill();
  }

  update () {
    this.drawProjectile();
    this.x = this.x + this.velocity.x;
    this.y = this.y + this.velocity.y;
  }
}


const friction = 0.99 // Picked .99 so that particles can go far
class Particle {
    constructor (x, y, radius, color, velocity) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.color = color;
      this.velocity = velocity;
      this.alpha = 1
    }

    drawParticle () {
        cntx.save()
        cntx.globalAlpha = this.alpha
        cntx.beginPath();
        cntx.arc(this.x, this.y, this
            .radius, 0, Math.PI * 2, false);
        cntx.fillStyle = this.color;
        cntx.fill();
        cntx.restore()
    }

    update () {
      this.drawParticle();
      this.velocity.x *= friction
      this.x = this.x + this.velocity.x;
      this.velocity.y *= friction
      this.y = this.y + this.velocity.y;
      this.alpha -= 0.01
    }
  }

const x = canvas.width / 2;
const y = canvas.height / 2;

const player = new Player(x, y, 10, 'white');

const projectiles = [];
const enemies = [];
const particles = [];

function spawnEnemies () {
  setInterval(() => {
    const radius = Math.random() * (30 - 5) + 5;

    let x;
    let y;
    if (Math.random() < 0.5) {
      // randomizing where enemies come from the right to left

      x = Math.random() < 0.5
        ? 0 - radius
        : canvas.width + radius;
      y = Math.random() * canvas.height;
    } else {
      // randomizing where enemies come from the left to right
      x = Math.random() * canvas.width;
      y = Math.random() < 0.5
        ? 0 - radius
        : canvas.height + radius;
    }

    const color = `hsl(${Math.random() * 360}, 50%, 50%)`;

    // setting velocity for enemy

    const angle = Math.atan2(
      canvas.height / 2 - y,
      canvas.width / 2 - x
    );

    const velocity = {
      x: Math.cos(angle),
      y: Math.sin(angle)
    };
    enemies.push(new Enemy(x, y, radius, color,
      velocity));
  }, 1000);
}

let animationId;

function animate () {
  animationId = requestAnimationFrame(animate);

  cntx.fillStyle = 'rgba(0, 0, 0, 0.1)';
  cntx.fillRect(0, 0, canvas.width, canvas.height);

  player.drawPlayer();

  particles.forEach((particle, index) => {
    if (particle.alpha <= 0) {
        particles.splice(index, 1)
    }else{
        particle.update()
    }
  });

  projectiles.forEach((projectile, index) => {
    projectile.update();

    // remove projectiles form edge of screen
    if (
      projectile.x + projectile.radius < 0 ||
            projectile.x - projectile.radius > canvas.width ||
            projectile.y + projectile.radius < 0 ||
            projectile.y - projectile.radius > canvas.height
    ) {
      setTimeout(() => {
        projectiles.splice(index, 1);
      }, 0);
    }
  });

  enemies.forEach((enemy, index) => {
    enemy.update();

    // dist between player and  enemy
    const dist = Math.hypot(player.x - enemy.x,
      player.y - enemy.y);

    // end game
    if (dist - enemy.radius - player.radius < 1) {
      cancelAnimationFrame(animationId);
    }

    // dist between projectile and enemy
    projectiles.forEach((projectile, projectileIndex) => {
      const dist = Math.hypot(projectile.x - enemy.x,
        projectile.y - enemy.y);

      // when projectile touch enemy
      if (dist - enemy.radius - projectile.radius < 1) {
        
        // create explosions
            for (let i = 0; i < enemy.radius * 2; i++) {

                particles.push(
                    new Particle(projectile.x,projectile.y,
                        Math.random() * 2,
                        enemy.color, {
                            // increasing the power of the particle explosion
                            x:(Math.random() - 0.5) * (Math.random() * 8),
                            y:(Math.random() - 0.5) * (Math.random() * 8)
                    })
                )
            }
            // removing splashing effect
            if (enemy.radius - 10 > 7) {
                gsap.to(enemy, {
                    radius: enemy.radius - 10
                })
            // removing projectile after hitting the enemy to shrink enemy
            setTimeout(() => {
                projectiles.splice(projectileIndex, 1);
            }, 0);
            } else {
            setTimeout(() => {
                enemies.splice(index, 1);
                projectiles.splice(projectileIndex, 1);
            }, 0);
            }
        }
    });
  });
}

addEventListener('click', (event) => {
// setting velocity for projectiles
  const angle = Math.atan2(
    event.clientY - canvas.height / 2,
    event.clientX - canvas.width / 2
  );

  const velocity = {
    x: Math.cos(angle) * 5,
    y: Math.sin(angle) * 5
  };

  projectiles.push(new Projectile(
    canvas.width / 2,
    canvas.height / 2,
    5, 'white', velocity)
  );
});

animate();
spawnEnemies();
