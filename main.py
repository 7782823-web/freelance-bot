#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bot import app

if __name__ == "__main__":
    print("🚀 Starting AI Free Lance Bot...")
    app.run(host="0.0.0.0", port=int(getenv("PORT", 5000)))

def getenv(name, default=None):
    import os
    return os.getenv(name, default)
