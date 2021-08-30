#!/usr/bin/env python3

from os import path

import config
import miraibot


if __name__ == "__main__":
    miraibot.init(config)
    miraibot.logger.info('导入内置插件中...')
    miraibot.load_builtin_plugins()
    miraibot.logger.info('导入外部插件中...')
    miraibot.load_plugins(
        path.join(path.dirname(__file__), 'plugins'),
        'plugins'
    )
    miraibot.run()
