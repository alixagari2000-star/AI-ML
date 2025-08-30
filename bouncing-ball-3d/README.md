# 3D Bouncing Ball Visualization

A beautiful 3D visualization of a ball bouncing inside a wireframe cube in slow motion. The application tracks bounces and stops after 20 bounces.

## Features

- **3D Wireframe Cube**: Transparent green wireframe cube as the boundary
- **Bouncing Ball**: Red ball with realistic physics and lighting
- **Slow Motion**: Ball moves in slow motion for better visualization
- **Bounce Counter**: Tracks the number of bounces (0-20)
- **Interactive Controls**: Start, stop, and reset functionality
- **Camera Controls**: Click and drag to rotate the view
- **Visual Effects**: Ball flashes yellow on each bounce
- **Modern UI**: Clean, modern interface with gradient backgrounds

## How to Run

1. **Open the HTML file**: Double-click `index.html` to open it in your web browser
2. **Alternative**: Right-click `index.html` and select "Open with" → Choose your preferred browser

## Controls

- **Start Animation**: Click the "Start Animation" button to begin the bouncing
- **Reset**: Click "Reset" to return the ball to the center and reset the bounce counter
- **Camera Rotation**: Click and drag anywhere on the screen to rotate the camera view
- **Window Resize**: The application automatically adjusts to window size changes

## Technical Details

- **Framework**: Three.js for 3D graphics
- **Physics**: Simple collision detection with velocity reversal
- **Lighting**: Ambient, directional, and point lighting for realistic effects
- **Performance**: Optimized rendering with requestAnimationFrame
- **Responsive**: Adapts to different screen sizes

## File Structure

```
bouncing-ball-3d/
├── index.html      # Main HTML file with UI
├── script.js       # JavaScript with Three.js implementation
└── README.md       # This file
```

## Browser Requirements

- Modern web browser with WebGL support
- Chrome, Firefox, Safari, or Edge recommended
- JavaScript enabled

## Customization

You can modify the following parameters in `script.js`:

- `this.maxBounces`: Change the number of bounces before stopping (default: 20)
- `this.velocity`: Adjust ball speed (default: 0.02 on all axes)
- `this.cubeSize`: Change cube size (default: 10)
- `this.ballRadius`: Change ball size (default: 0.5)

Enjoy the visualization! 🎾
