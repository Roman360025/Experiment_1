#include <stdint.h>

#ifndef VEMAC_H
#define VEMAC_H

typedef struct 
{	
	uint8_t mHdr;
	uint8_t fCtrl;
	uint16_t fcnt;
	uint8_t slots_id [10];
} vemac_header_t;

void serialize (vemac_header_t * header, uint8_t *message);
uint32_t  deserialize (uint8_t *message, vemac_header_t * header);

#endif