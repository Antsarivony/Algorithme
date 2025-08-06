from setuptools import setup, find_packages
setup(
    name="TikTok",
    version="1.0",
    description="Algorithme TikTok",
    author="Lariot",
    author_email="lariot.antsa@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'report-tiktok=TikTok.main:main'
        ]
    },
    python_requires=">=3.6",
)