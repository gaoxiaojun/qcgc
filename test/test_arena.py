from support import lib,ffi
from qcgc_test import QCGCTest

class ArenaTestCase(QCGCTest):
    def test_arena_size_calculations(self):
        exp = lib.QCGC_ARENA_SIZE_EXP
        size = 2**exp
        bitmap = size / 128
        cells = size / 16
        self.assertEqual(size, lib.qcgc_arena_size)
        self.assertEqual(bitmap, lib.qcgc_arena_bitmap_size)
        self.assertEqual(cells, lib.qcgc_arena_cells_count)

    def test_arena_create(self):
        p = lib.qcgc_arena_create()
        self.assertEqual(p, lib.qcgc_arena_addr(p))
        self.assertEqual(0, lib.qcgc_arena_cell_index(p))
        self.assertEqual(int(ffi.cast("uint64_t", p)),
                int(ffi.cast("uint64_t", p))
                    << lib.QCGC_ARENA_SIZE_EXP
                    >> lib.QCGC_ARENA_SIZE_EXP)

    def test_arena_size(self):
        self.assertEqual(lib.qcgc_arena_sizeof(), lib.qcgc_arena_size)

    def test_arena_layout(self):
        arena = lib.qcgc_arena_create()

        lib.arena_cells(arena)[0][0] = 15
        self.assertEqual(lib.arena_block_bitmap(arena)[0], 15)
        
        lib.arena_cells(arena)[lib.qcgc_arena_bitmap_size // 16][lib.qcgc_arena_bitmap_size % 16] = 3
        self.assertEqual(lib.arena_mark_bitmap(arena)[0], 3)

        lib.arena_cells(arena)[lib.qcgc_arena_cells_count - 1][15] = 12