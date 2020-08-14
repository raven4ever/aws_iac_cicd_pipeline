import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk"},
    packages=setuptools.find_packages(where="cdk"),

    install_requires=[
        "aws-cdk.core",
        "aws_cdk.aws_codecommit",
        "aws_cdk.aws_codebuild",
        "aws_cdk.aws_codedeploy",
        "aws_cdk.aws_codepipeline"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
