# -*- coding: utf-8 -*-
# Author    : ld
# Date      : 2022/12/1 9:49

import os
from loguru import logger
from config import BASE_DIR


log_file = os.path.join(BASE_DIR, "Log", "{time:YYYY}", "{time:MM}", "{time:DD}.log")

logger.add(log_file, rotation="00:00", encoding="utf-8")


