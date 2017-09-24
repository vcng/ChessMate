/*
 * Programmer: Miles Avelli
 * Date: 9/24/2017
 * class Protocol : used to communicate data to a Raspberry Pi where
 * game logic is processed and recieves commands to, for example, turn
 * on leds.
 */
class Protocol{
public:
    //Constructo, recieves a Stream reference s, mapping it to serial
    Protocol(Stream& s):serial(s){}

    //start is called inside the setup loop. It loops until the start command is recieved
    //from the Pi indicating it has booted and is ready for input.
    void start(){                 
      String input = "";                //String input empty
        while(true){                    //Loop until vaild input is received
          input = serial.readString();  //Read in string
          input.trim();                 //Trim '\n' or whitespace
          if(input == "start"){         //If input == "start", valid command
            go();                       //Send received command to Pi
            return;                     //break loop and return
          }
        }
    }
    
    //listener returns anything that is in the serial buffer as a String
    String listener(){
        return serial.readString();
    }
    
    //sends the go command to the Pi, used for confirming recieved input to the Pi
    void go(){
      serial.println("go");
    }
     //toggle takes a toggle string, in the form: "t r c", where r = row and c = col.
     //This is then sent to the Pi for processing.    
     void toggle(String input){
     serial.println(input);
    }
private:
   Stream& serial;  //Stream reference that holds the passed in reference in the constructor
};

//Create instance of Protocol class with Serial as the Stream
Protocol p(Serial);

//Below is the test driver

//Setup Loop, runs before main loop once
void setup() {
  Serial.begin(115200);       //Start Serial port with baud rate 115200, or 14.4 mbps
  delay(2000);                //Delay 2000ms, or 2 seconds
  p.start();                  //Call protocol start, will not return until sync'd with Pi
  delay(5000);                //Delay 5 seconds before breaking setup loop 
} 
//Global test variable count, used for generating values to emulate changes
int count = 0;

//Main Loop, loops until shutdown
void loop() {  
  //Below Strings are used for reading input and creating test output
  String in = "";
  String out = "t ";

  //Loop counts 10 times
  if(count < 10){
      count++;                    //Increment count
      out += count;               //Create output String
      out += " ";
      out += count+1;
      in = p.listener();          //Read from Pi
      if(in != ""){               //If in is not empty, i.e something was sent from Pi
        if(in[0] == 'l'){         //If in == l, which is an led command
          p.go();                 //Call protocol go, which tells Pi we recieved vaild input
          //led calls
          delay(500);             //Delay .5 seconds
        }else if(in[0] == 'r'){   //If in == r, then reset arduino
          p.go();                 
          //reset hardware call
          delay(500);
        }else if(in[0] == 'i'){   //If in == i, then initialize the board
          p.go();
          delay(5000);
        }
      }else{
        p.toggle(out);            //else send the toggle out
      }
  }else {
    count = 0;                    //reset count after 10 iterations
  }
}                                 //end of main loop
