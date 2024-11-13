<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frogger Game</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #eee;
        }
        #game {
            position: relative;
            width: 300px;
            height: 600px;
            background-color: #fff;
            border: 2px solid #333;
            overflow: hidden;
        }
        .frog {
            position: absolute;
            width: 30px;
            height: 30px;
            background-color: green;
        }
        .car {
            position: absolute;
            width: 50px;
            height: 30px;
            background-color: red;
        }
    </style>
</head>
<body>
    <div id="game">
        <div class="frog" id="frog" style="left: 135px; bottom: 0;"></div>
    </div>
    <script>
        const game = document.getElementById('game');
        const frog = document.getElementById('frog');
        const cars = [];
        let gameInterval;
        let carSpeed = 2;

        // Create cars
        function createCar() {
            const car = document.createElement('div');
            car.classList.add('car');
            car.style.left = Math.random() * (game.clientWidth - 50) + 'px';
            car.style.top = Math.random() * (game.clientHeight / 2) + 'px';
            game.appendChild(car);
            cars.push(car);
        }

        // Move cars
        function moveCars() {
            cars.forEach((car, index) => {
                let top = parseInt(car.style.top);
                top += carSpeed;
                if (top > game.clientHeight) {
                    car.remove();
                    cars.splice(index, 1);
                    createCar(); // Create a new car
                } else {
                    car.style.top = top + 'px';
                }
            });
        }

        // Check collision
        function checkCollision() {
            const frogRect = frog.getBoundingClientRect();
            cars.forEach(car => {
                const carRect = car.getBoundingClientRect();
                if (
                    frogRect.x < carRect.x + carRect.width &&
                    frogRect.x + frogRect.width > carRect.x &&
                    frogRect.y < carRect.y + carRect.height &&
                    frogRect.y + frogRect.height > carRect.y
                ) {
                    alert('Game Over!');
                    clearInterval(gameInterval);
                    resetGame();
                }
            });
        }

        // Reset game
        function resetGame() {
            cars.forEach(car => car.remove());
            cars.length = 0;
            gameInterval = null;
            frog.style.bottom = '0px';
        }

        // Control frog movement
        document.addEventListener('keydown', (event) => {
            const step = 30;
            if (event.key === 'ArrowUp') {
                frog.style.bottom = parseInt(frog.style.bottom) + step + 'px';
            } else if (event.key === 'ArrowDown') {
                frog.style.bottom = Math.max(0, parseInt(frog.style.bottom) - step) + 'px';
            } else if (event.key === 'ArrowLeft') {
                frog.style.left = Math.max(0, parseInt(frog.style.left) - step) + 'px';
            } else if (event.key === 'ArrowRight') {
                frog.style.left = Math.min(game.clientWidth - 30, parseInt(frog.style.left) + step) + 'px';
            }
        });

        // Start the game
        function startGame() {
            for (let i = 0; i < 5; i++) {
                createCar();
            }
            gameInterval = setInterval(() => {
                moveCars();
                checkCollision();
            }, 100);
        }

        startGame();
    </script>
</body>
</html>