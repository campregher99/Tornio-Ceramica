#ifndef CONFIG_H
#define CONFIG_H

//#define DEBUG	//enable debug mode if not commented
//#define MONITOR //enable monitoring mode if not commented
#include "Arduino.h"
#include "EEPROM.h"

//communication standard: "?/x/x/x!"
#define SEPARATOR '/'
#define STARTER "?"
#define ENDER '!'
#define OK_MSG "?OK!"
#define ERR_MSG "?ER!"
#define NOT_INI_EEP "?NE!"
#define INI_EEP "?IE!"

#define EEPROM_SIZE sizeof(float) * 5 + sizeof(int) * 1 + sizeof(uint64_t)  //32 bytes for PID
#define EEPROM_SIZE sizeof(float) * 40 + sizeof(int) * 3 + sizeof(uint64_t) + sizeof(int) * 2 	//188 bytes for controller

//PWM parameter
#define FREQ_PWM 3000
#define CHANNEL_PWM 0
#define RESOLUTION_PWM 10
#define PIN_PWM 16

#endif
