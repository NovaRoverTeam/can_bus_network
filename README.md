This Can_bus network has not been integrated with the rest of the rover, aptly named placeholder topics have been utilised.
To test this using virtual cans run by socketcan you can start up two virtual can channels by running bash scripts/sim/run_can

The CanTX node listens for motor msgs published on the /motors/arm and motors/drive topics, translates them into a can message, gives it an id based on the scripts/can_network_scripts/can_id.py file and sends it onto the canTX bus.

The CanRX node receives all can msgs on the CanRX bus and sorts them by ID. This includes the sensor information as well as the report information from the other nodes. It then translates the can message into an appropriate msg type for ros and publishes it into the correct topic.

Launch can_nodes.launch to run both the nodes as well as a placeholder publisher publishing onto the motor topics. 


