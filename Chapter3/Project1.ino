void setup() {
  Serial.begin(9600);
 pinMode(13, OUTPUT); 
 pinMode(12, OUTPUT);
}

void loop() {
  char a = Serial.read();
  if (a == '0')
    {digitalWrite(13, 0);
    digitalWrite(12, 0);}
  else if (a == '1')
  { digitalWrite(13, 1);
   digitalWrite(12, 1);}
    else if (a == '2')
  { digitalWrite(13, 1);
   digitalWrite(12, 0);}
    else if (a == '3')
  { digitalWrite(13, 0);
   digitalWrite(12, 1);}
  else if (a == '4')
   { digitalWrite(13, 1);
   digitalWrite(12, 0);
    delay(1000);
    digitalWrite(13, 0);
    digitalWrite(12, 1);
    delay(1000);
     digitalWrite(13, 1);
   digitalWrite(12, 0);
    delay(1000);
    digitalWrite(13, 0);
    digitalWrite(12, 1);
    delay(1000);
   }
 
  delay(10);
 
  
  
}
