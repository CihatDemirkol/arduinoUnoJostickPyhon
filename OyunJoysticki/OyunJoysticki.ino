int yukari;//1 degeri göndersin
int sag;//2 degeri göndersin
int sol; //3 degeri göndersin
int bos;
int ustSag;
int ustSol;
void setup() {
  Serial.begin(9600, SERIAL_8N1); // 8 veri biti, hiçbir çiftleme, 1 stop biti ile seri iletişim

}

void loop() {
  int xValue = analogRead(A0); // Joystick'in X eksenini oku
  int yValue = analogRead(A1); // Joystick'in Y eksenini oku
  Serial.print(xValue);
  Serial.print(",");
  Serial.println(yValue);

  if (yValue == 1023 && xValue == 0) //ustSol

  {
    ustSol = 5;
    Serial.println(ustSol);
  }
  else if (yValue == 0 && xValue == 0) //ustsag

  {
    ustSag = 6;
    Serial.println(ustSag);
  }

  else if (xValue == 0)
  { //yukarı
    yukari = 1;
    Serial.println(yukari);
  }
  else if (yValue == 0)
  { //sağ
    sag = 2;
    Serial.println(sag);
  }
  else if (yValue == 1023) //sol

  {
    sol = 3;
    Serial.println(sol);
  }


  else
  {
    bos = 4;
    Serial.println(bos);
  }
  delay(100); // Veri gönderim hızını ayarlayabilirsiniz
}
