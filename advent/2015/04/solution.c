#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <mhash.h>

typedef uint8_t u8;

int main(void) {
  char buf[100];

  for (int i = 1; true; i++) {
    MHASH state = mhash_init(MHASH_MD5);
    int n = sprintf(buf, "%s%d", "iwrupvqb", i);
    mhash(state, buf, n);
    u8 *res = mhash_end(state);

  //if (res[0] == 0 && res[1] == 0 && res[2] == 0) {
    if (res[0] == 0 && res[1] == 0 && res[2] >> 4 == 0) {
      printf("%d\n", i);
      return 0;
    }
  }

  assert(false);
}
