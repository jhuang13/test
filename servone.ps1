function ConnectIExplorer() {    param($HWND)
    $objShellApp = New-Object -ComObject Shell.Application     try {      $EA = $ErrorActionPreference; $ErrorActionPreference = 'Stop'      $objNewIE = $objShellApp.Windows() | ?{$_.HWND -eq $HWND}      $objNewIE.Visible = $true    } catch {      #it may happen, that the Shell.Application does not find the window in a timely-manner, therefore quick-sleep and try again      Write-Host "Waiting for page to be loaded ..."       Start-Sleep -Milliseconds 500      try {        $objNewIE = $objShellApp.Windows() | ?{$_.HWND -eq $HWND}        $objNewIE.Visible = $true      } catch {        Write-Host "Could not retreive the -com Object InternetExplorer. Aborting." -ForegroundColor Red        $objNewIE = $null      }         } finally {       $ErrorActionPreference = $EA      $objShellApp = $null    }    return $objNewIE  } 
function Fill() {    param(    $ie,    $keyworkd,    [switch]$name,    $fill,    $frame    )
    sleep -Milliseconds 1000
    while (-not ($ie.Readystate -eq 4)){         echo "in"        sleep -Milliseconds 1000     }
    $document = $ie.document
    if ($frame){        $document = $ie.Document.getElementById($frame).contentWindow.document    }
    if ($name){        $document.getElementsByName($keyworkd)[0].Value = $fill    }else{        $document.getElementByID($keyworkd).Value = $fill    }
}
function Click() {    param(    $ie,    $keyworkd,    [switch]$name,    $frame    )
    sleep -Milliseconds 1000        while (-not ($ie.Readystate -eq 4)){         echo "in"        sleep -Milliseconds 1000     }
    $document = $ie.document
    if ($frame){        $document = $ie.Document.getElementById($frame).contentWindow.document    }
    if ($name){        $document.getElementsByName($keyworkd)[0].Click()    }else{        $document.getElementByID($keyworkd).Click()    }
}

$HWND = ($objIE = New-Object -ComObject InternetExplorer.Application).HWND$objIE.Navigate("https://sevone.hk.hsbc/#login")$objIE = ConnectIExplorer -HWND $HWND
Fill -ie $objIE -keyworkd "login" -frame "domino64" -fill "44090993"
Fill -ie $objIE -keyworkd "passwd" -frame "domino64" -fill "ibcn@OCT2017"
Click -ie $objIE -keyworkd "ext-gen17" -frame "domino64"
sleep -Milliseconds 1000    while (-not ($objIE.Readystate -eq 4)){     echo "in"    sleep -Milliseconds 1000 }
$objIE.Document.getElementById("domino27").contentWindow.document.getElementById("ext-gen16").getElementsByTagName("a")[0].Click()
