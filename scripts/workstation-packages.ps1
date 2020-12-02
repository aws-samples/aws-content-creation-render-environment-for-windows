[cmdletbinding()]
Param()


try {
    $ErrorActionPreference = "Stop"

    #
    # Install packages
    #
    Write-Verbose "Install Chocolatey"
    $url = 'https://chocolatey.org/install.ps1'
    Invoke-Expression ((new-object net.webclient).DownloadString($url))

    Write-Host "Install 7zip"
    choco install --limit-output -y 7zip

    Write-Host "Install awscli"
    choco install --limit-output -y awscli

    Write-Host "Install Firefox"
    choco install --limit-output -y firefox

    Write-Host "Install Blender"
    choco install --limit-output -y blender

    Write-Host "choco installs complete"
}
catch {
    Write-Host "catch: $_"
    $_ | Write-AWSQuickStartException
}
