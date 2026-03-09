#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OpenClaw Tutorial 项目安装脚本
"""

from setuptools import setup, find_packages
import os

# 读取README内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements.txt
def read_requirements():
    requirements = []
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        with open(req_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)
    return requirements

setup(
    name="openclaw-tutorial",
    version="1.0.0",
    author="lsq-web17",
    author_email="arringtondhuka@gmail.com",
    description="OpenClaw实战教程系列",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsq-web17/OpenClaw-Tutorial",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings[python]>=0.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "openclaw-hello=examples.hello-world.hello_skill:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=["openclaw", "ai-assistant", "tutorial", "automation"],
    project_urls={
        "Homepage": "https://github.com/lsq-web17/OpenClaw-Tutorial",
        "Repository": "https://github.com/lsq-web17/OpenClaw-Tutorial",
        "Documentation": "https://lsq-web17.github.io/OpenClaw-Tutorial",
        "Issues": "https://github.com/lsq-web17/OpenClaw-Tutorial/issues",
    },
)