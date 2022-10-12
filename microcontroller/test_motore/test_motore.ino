#include <Queue.h>

#include "Function.h"
#include "Config.h"

void output(float _output);

void setup() {
  Serial.begin(115200);
  // put your setup code here, to run once:
  // configure LED PWM functionalitites
  ledcSetup(CHANNEL_PWM, FREQ_PWM, RESOLUTION_PWM);

  // attach the channel to the GPIO to be controlled
  ledcAttachPin(PIN_PWM, CHANNEL_PWM);

  output(0);
  wait_serial();
  Serial.println("input,output");
}
float ref=0;
Queue input(10);
void loop() {
  input.push(analogRead(4));
  Serial.print(input.mean());
  Serial.print(",");
  Serial.println(ref);
  if (Serial.available())
  {
    ref = Serial.readStringUntil(ENDER).toFloat();
    clear_in_buffer();
    if(ref>=0&&ref<=100)
    {
      output(ref);
    }
      
      
  }

}

void output(float _output)
{
#ifdef MONITOR
  static bool is_first = true;
  if (is_first)
  {
    delayMicroseconds(180);
  } else
  {
    Serial.println(_output);
  }
  is_first = false;
#endif
  ledcWrite(CHANNEL_PWM, _output * (pow(2, RESOLUTION_PWM) - 1) / 100);
}
