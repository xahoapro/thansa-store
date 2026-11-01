"""Paths for the code-pack tests of thansa.zalo, and server/ of Thansa OS on sys.path.

The plugins in this pack run INSIDE a Thansa OS server and import its modules (`zalo_cli`, `image_gen`,
`image_vision`, `conversations`), so their tests need a Thansa OS checkout next to this repo. CI clones it;
locally point THANSA_OS_DIR at yours (default: ../thansa-os next to this repo).

    THANSA_OS_DIR=/path/to/thansa-os python tests/thansa.zalo/test_zalo_read_images.py
"""
import os
import sys
from pathlib import Path

STORE = Path(__file__).resolve().parents[2]
PACK = STORE / "packs" / "thansa.zalo"
ROOT = Path(os.environ.get("THANSA_OS_DIR") or (STORE.parent / "thansa-os")).resolve()
SERVER = ROOT / "server"
if not (SERVER / "zalo_cli.py").is_file():
    raise SystemExit(f"Thansa OS checkout not found at {ROOT} (set THANSA_OS_DIR)")
if str(SERVER) not in sys.path:
    sys.path.insert(0, str(SERVER))
