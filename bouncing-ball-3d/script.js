class BouncingBall3D {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.ball = null;
        this.cube = null;
        this.velocity = new THREE.Vector3(
            (Math.random() - 0.5) * 1.0,
            (Math.random() - 0.5) * 1.0,
            (Math.random() - 0.5) * 1.0
        );
        this.position = new THREE.Vector3(0, 0, 0);
        this.bounceCount = 0;
        this.maxBounces = 20;
        this.isAnimating = false;
        this.animationId = null;
        
        this.cubeSize = 10;
        this.ballRadius = 0.5;
        
        this.init();
        this.setupEventListeners();
    }

    init() {
        // Create scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x1a1a2e);

        // Create camera
        this.camera = new THREE.PerspectiveCamera(
            75,
            window.innerWidth / window.innerHeight,
            0.1,
            1000
        );
        this.camera.position.set(15, 15, 15);
        this.camera.lookAt(0, 0, 0);

        // Create renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        document.getElementById('container').appendChild(this.renderer.domElement);

        // Create cube (wireframe)
        this.createCube();
        
        // Create ball
        this.createBall();
        
        // Add lighting
        this.addLighting();
        
        // Start render loop
        this.animate();
    }

    createCube() {
        const geometry = new THREE.BoxGeometry(this.cubeSize, this.cubeSize, this.cubeSize);
        const material = new THREE.MeshBasicMaterial({
            color: 0x00ff88,
            wireframe: true,
            transparent: true,
            opacity: 0.8
        });
        
        this.cube = new THREE.Mesh(geometry, material);
        this.scene.add(this.cube);
    }

    createBall() {
        const geometry = new THREE.SphereGeometry(this.ballRadius, 32, 32);
        const material = new THREE.MeshPhongMaterial({
            color: 0xff6b6b,
            shininess: 100,
            specular: 0x444444
        });
        
        this.ball = new THREE.Mesh(geometry, material);
        this.ball.castShadow = true;
        this.ball.receiveShadow = true;
        this.scene.add(this.ball);
        
        // Set initial position
        this.ball.position.copy(this.position);
    }

    addLighting() {
        // Ambient light
        const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
        this.scene.add(ambientLight);

        // Directional light
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(10, 10, 5);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 2048;
        directionalLight.shadow.mapSize.height = 2048;
        this.scene.add(directionalLight);

        // Point light for ball glow
        const pointLight = new THREE.PointLight(0xff6b6b, 0.5, 10);
        pointLight.position.set(0, 0, 0);
        this.scene.add(pointLight);
    }

    updateBallPhysics() {
        if (!this.isAnimating) return;

        // Update position
        this.position.add(this.velocity);
        this.ball.position.copy(this.position);

        // Check for collisions with cube walls
        const halfSize = this.cubeSize / 2;
        const ballPos = this.position;
        
        // X-axis collision
        if (ballPos.x + this.ballRadius > halfSize || ballPos.x - this.ballRadius < -halfSize) {
            this.velocity.x *= -1;
            // Add some randomness to Y and Z velocity on X-axis bounce
            this.velocity.y += (Math.random() - 0.5) * 0.01;
            this.velocity.z += (Math.random() - 0.5) * 0.01;
            this.bounceCount++;
            this.updateUI();
            this.createBounceEffect();
        }
        
        // Y-axis collision
        if (ballPos.y + this.ballRadius > halfSize || ballPos.y - this.ballRadius < -halfSize) {
            this.velocity.y *= -1;
            // Add some randomness to X and Z velocity on Y-axis bounce
            this.velocity.x += (Math.random() - 0.5) * 0.01;
            this.velocity.z += (Math.random() - 0.5) * 0.01;
            this.bounceCount++;
            this.updateUI();
            this.createBounceEffect();
        }
        
        // Z-axis collision
        if (ballPos.z + this.ballRadius > halfSize || ballPos.z - this.ballRadius < -halfSize) {
            this.velocity.z *= -1;
            // Add some randomness to X and Y velocity on Z-axis bounce
            this.velocity.x += (Math.random() - 0.5) * 0.01;
            this.velocity.y += (Math.random() - 0.5) * 0.01;
            this.bounceCount++;
            this.updateUI();
            this.createBounceEffect();
        }

        // Check if max bounces reached
        if (this.bounceCount >= this.maxBounces) {
            this.stopAnimation();
            document.getElementById('status').textContent = 'Animation completed!';
        }
    }

    createBounceEffect() {
        // Create a temporary flash effect
        const originalColor = this.ball.material.color.getHex();
        this.ball.material.color.setHex(0xffff00);
        
        setTimeout(() => {
            this.ball.material.color.setHex(originalColor);
        }, 100);
    }

    updateUI() {
        document.getElementById('bounce-counter').textContent = `Bounces: ${this.bounceCount} / ${this.maxBounces}`;
    }

    animate() {
        this.animationId = requestAnimationFrame(() => this.animate());
        
        // Update ball physics
        this.updateBallPhysics();
        
        // Render scene
        this.renderer.render(this.scene, this.camera);
    }

    startAnimation() {
        this.isAnimating = true;
        this.bounceCount = 0;
        this.updateUI();
        document.getElementById('status').textContent = 'Animation running...';
        document.getElementById('startBtn').disabled = true;
    }

    stopAnimation() {
        this.isAnimating = false;
        document.getElementById('startBtn').disabled = false;
    }

    reset() {
        this.stopAnimation();
        this.bounceCount = 0;
        this.position.set(0, 0, 0);
        this.velocity.set(
            (Math.random() - 0.5) * 1.0,
            (Math.random() - 0.5) * 1.0,
            (Math.random() - 0.5) * 1.0
        );
        this.ball.position.copy(this.position);
        this.updateUI();
        document.getElementById('status').textContent = 'Ready to start';
    }

    setupEventListeners() {
        document.getElementById('startBtn').addEventListener('click', () => {
            this.startAnimation();
        });

        document.getElementById('resetBtn').addEventListener('click', () => {
            this.reset();
        });

        // Handle window resize
        window.addEventListener('resize', () => {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
        });

        // Add mouse controls for camera rotation
        let isMouseDown = false;
        let mouseX = 0;
        let mouseY = 0;

        document.addEventListener('mousedown', (event) => {
            isMouseDown = true;
            mouseX = event.clientX;
            mouseY = event.clientY;
        });

        document.addEventListener('mouseup', () => {
            isMouseDown = false;
        });

        document.addEventListener('mousemove', (event) => {
            if (isMouseDown) {
                const deltaX = event.clientX - mouseX;
                const deltaY = event.clientY - mouseY;
                
                // Rotate camera around the scene
                const spherical = new THREE.Spherical();
                spherical.setFromVector3(this.camera.position);
                spherical.theta -= deltaX * 0.01;
                spherical.phi += deltaY * 0.01;
                spherical.phi = Math.max(0.1, Math.min(Math.PI - 0.1, spherical.phi));
                
                this.camera.position.setFromSpherical(spherical);
                this.camera.lookAt(0, 0, 0);
                
                mouseX = event.clientX;
                mouseY = event.clientY;
            }
        });
    }
}

// Initialize the application when the page loads
window.addEventListener('load', () => {
    new BouncingBall3D();
});
