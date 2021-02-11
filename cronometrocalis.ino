
unsigned long time;
#include <TimerOne.h>
unsigned char segundos =0;
unsigned char minutos = 0;
unsigned char horas = 0;
void timer1s()
{
  
  if(segundos == 59)
 {
  segundos = 0;
  minutos++;
 }
  else 
  segundos++;
 
 if(minutos == 59)
 horas++;
 else 
 horas=horas;
  
}
void setup()
{

  Serial.begin(9600);
 Timer1.initialize(1000000);
 Timer1.attachInterrupt(timer1s);
}

void loop()
{

if(horas<10)
{
  Serial.print(0);
}
  Serial.print( horas);
  
  Serial.print(": ");
  if(minutos<10)
{
  Serial.print(0);
}
  Serial.print(minutos);
  Serial.print(": ");
  if(segundos<10)
 {
  Serial.print(0);
  }
  Serial.print(segundos);
  Serial.print('\n');
  
delay(1000);
}

  
 
