# IRT Sensors Bring-Up Package

[![License](https://img.shields.io/badge/license-BSD--3-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<!--- protected region package header begins -->
**Author:**
- Maximilian Nitsch <maximilian.nitsch@rwth-aachen.de> (Institute of Automatic Control - RWTH Aachen University)

**Maintainer:**
  - Maximilian Nitsch <maximilian.nitsch@rwth-aachen.de> (Institute of Automatic Control - RWTH Aachen University)
<!--- protected region package header ends -->

## Description
This project provides a ROS 2 package that launches the following navigation sensor ROS 2 nodes:

- [IMU-Simulator](https://github.com/maximilian-nitsch/IMU-Simulator)
- [Magnetometer-Simulator](https://github.com/maximilian-nitsch/Magnetometer-Simulator)
- [DVL-Simulator](https://github.com/maximilian-nitsch/DVL-Simulator)
- [USBL-Simulator](https://github.com/maximilian-nitsch/USBL-Simulator)
- [Depth-Pressure-Sensor-Simulator](https://github.com/maximilian-nitsch/Depth-Pressure-Sensor-Simulator)

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Coding Guidelines](#coding-guidelines)
- [Contributing](#contributing)
- [License](#license)

# Dependencies

This project depends on the following literature and libraries:

- **ROS 2 Humble**: ROS 2 is a set of software libraries and tools for building robot applications: [ROS 2 Installation page](https://docs.ros.org/en/humble/Installation.html)).


# Installation

To install the `sensors_bringup_package`, you need to follow these steps:

1. **Install ROS 2 Humble**: Make sure you have ROS 2 (Humble) installed. You can follow the official installation instructions provided by ROS 2. Visit [ROS 2 Humble Installation page](https://docs.ros.org/en/humble/Installation.html) for detailed installation instructions tailored to your platform.

2. **Clone the Package**: Clone the package repository to your ROS 2 workspace. If you don't have a ROS 2 workspace yet, you can create one using the following commands:

    ```bash
    mkdir -p /path/to/ros2_workspace/src
    cd /path/to/ros2_workspace/src
    ```

    Now, clone the package repository:

    ```bash
    git clone <repository_url>
    ```

    Replace `<repository_url>` with the URL of your package repository.

3. **Build the Package**: Once the package is cloned, you must build it using colcon, the default build system for ROS 2. Navigate to your ROS 2 workspace and run the following command:

    ```bash
    cd /path/to/ros2_workspace
    colcon build
    ```

    This command will build all the packages in your workspace, including the newly added package.

4. **Source the Workspace**: After building the package, you need to source your ROS 2 workspace to make the package available in your ROS 2 environment. Run the following command:

    ```bash
    source /path/to/ros2_workspace/install/setup.bash
    ```

    Replace `/path/to/ros2_workspace` with the actual path to your ROS 2 workspace.

That's it! Your `sensors_bringup_package` should now be installed along with its dependencies and ready to use in your ROS 2 environment.

## Usage

1. **Start the Sensors BringUp Package** with the launch file:
    ```bash
    ros2 launch sensors_bringup_package sensor_simulators.launch.py
    ```
    
## Coding Guidelines

This project follows these coding guidelines:
- https://google.github.io/styleguide/cppguide.html
- http://docs.ros.org/en/humble/The-ROS2-Project/Contributing/Code-Style-Language-Versions.html 


## Contributing

If you want to contribute to the project, see the [CONTRIBUTING](CONTRIBUTING) file for details.

## License

This project is licensed under the BSD-3-Clause License. See the [LICENSE](LICENSE) file for details.
