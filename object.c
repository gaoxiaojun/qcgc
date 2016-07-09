#include "object.h"

#include <assert.h>
#include <stddef.h>

#include "arena.h"

void qcgc_write(object_t *object) {
#if CHECKED
	assert(object != NULL);
#endif
	if ((object->flags & QCGC_GRAY_FLAG) != 0) {
		object->flags |= QCGC_GRAY_FLAG;
		if (qcgc_arena_get_blocktype((cell_t *) object) == BLOCK_BLACK) {
			// This was black before, push it to gray stack again
			arena_t *arena = qcgc_arena_addr((cell_t *) object);

			// TODO: Push to gray stack
		}
	}
}