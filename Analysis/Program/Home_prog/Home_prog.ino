#include <ESP8266WiFi.h>
 
const char* ssid = "NETGEAR74";
const char* password = "87654321";
IPAddress staticIP(10,0,0,20);
IPAddress gateway(10,0,0,20);
IPAddress subnet(255,255,255,0);
int ledPin = 0;
int ledPin1 = 2;
WiFiServer server(80);
 
void setup() {
  Serial.begin(115200);
  delay(10);
 
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin1, OUTPUT);
  digitalWrite(ledPin, LOW);
  digitalWrite(ledPin1, LOW);
 
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
  WiFi.config(staticIP, gateway, subnet);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
 
}
 
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
 
  // Match the request
 
  int value = LOW;
  if (request.indexOf("/LED=ON") != -1)  {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin1, HIGH);
    value = HIGH;
  }
  if (request.indexOf("/LED=OFF") != -1)  {
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin1, LOW);
    value = LOW;
  }
  if (request.indexOf("/LED1=ON") != -1)  {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin1, LOW);
    value = HIGH;
  }
  if (request.indexOf("/LED2=ON") != -1)  {
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin, LOW);
    value = HIGH;
  }
// Set ledPin according to the request
//digitalWrite(ledPin, value);
 
  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
 
  client.print("Led pin is now: ");
 
  if(value == HIGH) {
    client.print("On");
  } else {
    client.print("Off");
  }
  client.println("<br><br>");
  client.println("&emsp;<a href=\"/LED=ON\"\"><button>ALL APPLIANCE</button></a><br />");
  client.println("<a href=\"/LED2=ON\"\"><button>LIGHT 1 </button></a>");
  client.println("&ensp;<a href=\"/LED1=ON\"\"><button>LIGHT 2</button></a><br />");
  client.println("&emsp;&ensp;&nbsp;<a href=\"/LED=OFF\"\"><button>ALL OFF</button></a>");  
  client.println("</html>");
 
  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
 
}
 