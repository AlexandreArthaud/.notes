# C#

## Dotnet

After you've install .NET, the **dotnet.exe** (sometimes also available just as **dotnet**) tool
will be available in Command Line. You can use it to generate, build or execute various C# projects.
It can also be used to check the current .NET version, whether you could update .NET and more.

```logm
dotnet command to check current .NET version : dotnet --version
dotnet command to check whether a new .NET version is available : dotnet sdk check
dotnet command to generate a C# project based on a {template} (there are many templates) : dotnet new template
  dotnet new [template] for a console application : console
  dotnet new [template] for a class library : classlib
  dotnet new [template] for a WPF application : wpf
dotnet command to build (compile) a .NET project from its folder : dotnet build
dotnet command to run a .NET project from its folder : dotnet run
```