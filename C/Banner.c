#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>


void File()
{
  char Filename[256];
  printf("Enter the name of the file you wish to use");
  scanf("%s", &Filename);
  FILE *in = fopen(Filename, "r");
  if (in == NULL) printf("File does not exist..goddamn it.\n");
  else printf("File is being read.");
}


void scan(int port, char host[]);

int main(int argc, char **argv)
{
  char host[100];
  char *p;
  int ports[10];
  int i = 0;
  int var;
  char space[] = " ,";

  if (argc < 2){
    fprintf(stderr, "[++]Use: %s <hostname> <port , port, port>\n", argv[0]);
    exit(0);
  }

  p = strtok(argv[2], space);
  strcpy(host, argv[1]);
  while(p != NULL) {
    sscanf(p, "%d", &var);
    ports[i++] = var;
    p = strtok(NULL, space);
  }

}
