import rclpy
from rclpy.node import Node
from eyes_disp_system_node.serialModule.serial_val import SerialUART

from eyes_msgs.msg import Eyes

class EyeInfoSubscriber(Node):
    

    def __init__(self, debug_disp, board):
        super().__init__('eyes_disp_system_node')
        self.declare_parameter('port_name','/dev/ttyACM0')
        self.declare_parameter('bps_speed', 9600)
        #Read parameters 
        self.port_name = self.get_parameter('port_name').get_parameter_value().string_value
        self.bps_speed = self.get_parameter('bps_speed').get_parameter_value().integer_value
        #Set init
        self.subscription = self.create_subscription(Eyes, 'eye_info_topic', self.listener_callback, 10)
        self.board = board
        self.disp = debug_disp
        if self.board == True:
            self.subscription
            self.ser = SerialUART(self.port_name, self.bps_speed,  timeOut=None, debaug=False)
            self.get_logger().info('port = "%s"' % self.port_name)
            self.get_logger().info('speed = "%s"' % self.bps_speed)
        self.get_logger().info("Finish init")

    def listener_callback(self, msg):
        #Save the value of eyes_msgs
        self.eye_lid_l = msg.eye_lid_l
        self.eye_lid_r = msg.eye_lid_r
        self.eye_pupil_l = msg.eye_pupil_l
        self.eye_pupil_r = msg.eye_pupil_r
        self.eye_blink = msg.eye_blink
        #Whe if "disp" is True, disp logger save vaues
        if self.disp == True:
            self.get_logger().info("===========================")
            self.get_logger().info('eye_lid_l : "%d"' % self.eye_lid_l)
            self.get_logger().info('eye_lid_r : "%d"' % self.eye_lid_r)
            self.get_logger().info('eye_pupil_l : "%d"' % self.eye_pupil_l)
            self.get_logger().info('eye_pupil_r : "%d"' % self.eye_pupil_r)
            self.get_logger().info('eye_blink : "%d"' % self.eye_blink)
            self.get_logger().info("===========================")
        if self.board == True:
            self.get_logger().info("Send Arduino board ...")
            #Send message contents saved in Arduino board
            self._SendScurely('eye_lid_l:' + str(self.eye_lid_l))
            self._SendScurely('eye_lid_r:' + str(self.eye_lid_r))
            self._SendScurely('eye_pupil_l:' + str(self.eye_pupil_l))
            self._SendScurely('eye_pupil_r:' + str(self.eye_pupil_r))
            self._SendScurely('eye_blink:' + str(self.eye_blink))
            self._SendScurely('finish')
            self.get_logger().info("Finished send Arduino board !!")
    
    def _SendScurely(self,dataString,times=None):
        success = False
        i = 0
        if times == None:
            while success == False:
                self.ser.writeStrln(dataString)
                if dataString == self.ser.readStr():
                    success = True
        else:
            while success == False and i < (times+1):
                self.ser.writeStrln(dataString)
                if dataString == self.ser.readStr():
                    success = True
        return success



    def pyserial_colse(self):
        self.ser.close()

def main(args=None):
    print('Hi from eyes_disp_system_node.')
    rclpy.init(args=args)
    eyeSystem = EyeInfoSubscriber(debug_disp = True, board=True)
    rclpy.spin(eyeSystem)
    eyeSystem.pyserial_colse()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
