# Design Document

## Overview

The self-driving car system will be implemented as a Python simulation using object-oriented design principles. The system consists of a Car class with integrated sensors, a simple rule-based decision engine, an Environment class to manage obstacles and boundaries, and a Visualization component using pygame for real-time display.

The architecture follows a sense-think-act paradigm where the car continuously senses its environment, processes the information to make decisions, and acts by adjusting its steering and movement.

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Environment   │    │      Car        │    │  Visualization  │
│                 │    │                 │    │                 │
│ - Obstacles     │◄───┤ - Position      │────┤ - Display       │
│ - Boundaries    │    │ - Sensors       │    │ - Real-time     │
│ - Collision     │    │ - Decision      │    │ - Interactive   │
│   Detection     │    │   Engine        │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Simulation    │
                    │    Manager      │
                    │                 │
                    │ - Game Loop     │
                    │ - Time Step     │
                    │ - Configuration │
                    └─────────────────┘
```

## Components and Interfaces

### Car Class
- **Position and Movement**: Tracks x, y coordinates, heading angle, and velocity
- **Sensor System**: Simulates distance sensors in multiple directions (front, front-left, front-right)
- **Decision Engine**: Rule-based system that processes sensor data and determines steering actions
- **Control System**: Applies steering decisions to update heading and position

**Key Methods:**
- `update()`: Main update loop for sense-think-act cycle
- `sense_environment()`: Detects obstacles and calculates distances
- `make_decision()`: Processes sensor data and determines steering action
- `apply_controls()`: Updates position and heading based on decisions

### Environment Class
- **Obstacle Management**: Stores and manages static obstacles
- **Boundary Handling**: Defines simulation area boundaries
- **Collision Detection**: Provides distance calculations between car and obstacles
- **Spatial Queries**: Efficient obstacle detection within sensor range

**Key Methods:**
- `add_obstacle()`: Adds obstacles to the environment
- `get_distance_to_obstacles()`: Returns distances from a point to nearby obstacles
- `is_collision()`: Checks if car position collides with obstacles
- `get_boundaries()`: Returns environment boundary information

### Sensor System
- **Range-based Detection**: Simulates LIDAR-like distance sensors
- **Multi-directional Sensing**: Sensors at different angles (0°, -30°, +30°)
- **Distance Calculation**: Uses geometric calculations for obstacle detection
- **Sensor Configuration**: Adjustable range and angular resolution

### Decision Engine
- **Rule-based Logic**: Simple if-then rules for obstacle avoidance
- **Priority System**: Handles multiple obstacles by prioritizing closest threats
- **Steering Commands**: Outputs steering angle adjustments
- **Safety Margins**: Maintains safe distances from obstacles

**Decision Rules:**
1. If obstacle ahead and clear on right → steer right
2. If obstacle ahead and clear on left → steer left  
3. If obstacle ahead and blocked both sides → reverse or stop
4. If no obstacles → maintain straight course

### Visualization System
- **Real-time Display**: Uses pygame for smooth animation
- **Car Representation**: Visual car with directional indicator
- **Obstacle Rendering**: Clear obstacle visualization
- **Sensor Visualization**: Optional display of sensor rays and detection zones
- **Information Overlay**: Speed, sensor readings, and decision status

## Data Models

### Car State
```python
class CarState:
    x: float           # X position
    y: float           # Y position  
    heading: float     # Heading angle in radians
    velocity: float    # Current speed
    steering_angle: float  # Current steering input
```

### Sensor Reading
```python
class SensorReading:
    angle: float       # Sensor direction relative to car
    distance: float    # Distance to nearest obstacle
    obstacle_detected: bool  # Whether obstacle is within range
```

### Obstacle
```python
class Obstacle:
    x: float          # X position
    y: float          # Y position
    radius: float     # Collision radius
    type: str         # Obstacle type (for future extension)
```

## Error Handling

### Collision Detection
- **Boundary Violations**: Handle car moving outside environment bounds
- **Obstacle Collisions**: Detect and respond to car-obstacle intersections
- **Sensor Failures**: Graceful degradation if sensor calculations fail

### Configuration Validation
- **Parameter Bounds**: Validate speed, sensor range, and environment size parameters
- **Obstacle Placement**: Ensure obstacles are placed within environment boundaries
- **Default Fallbacks**: Use safe default values for invalid configurations

### Runtime Errors
- **Division by Zero**: Handle edge cases in distance and angle calculations
- **Infinite Loops**: Prevent car from getting stuck in oscillating behavior
- **Memory Management**: Efficient handling of sensor data and visualization updates

## Testing Strategy

### Unit Tests
- **Car Movement**: Test position updates, heading changes, and velocity control
- **Sensor Calculations**: Verify distance calculations and obstacle detection accuracy
- **Decision Logic**: Test steering decisions for various obstacle configurations
- **Environment**: Test obstacle management and collision detection

### Integration Tests
- **Sense-Think-Act Cycle**: Test complete car behavior loop
- **Environment Interaction**: Test car behavior with multiple obstacles
- **Boundary Handling**: Test car behavior at environment edges
- **Visualization Integration**: Test display updates and user interaction

### Simulation Tests
- **Scenario-based Testing**: Test predefined obstacle courses
- **Performance Testing**: Ensure smooth real-time operation
- **Configuration Testing**: Test various parameter combinations
- **Edge Case Testing**: Test extreme scenarios (dense obstacles, tight spaces)

### Test Data
- **Simple Scenarios**: Single obstacle avoidance
- **Complex Scenarios**: Multiple obstacles requiring path planning
- **Boundary Scenarios**: Navigation near environment edges
- **Stress Scenarios**: High obstacle density environments