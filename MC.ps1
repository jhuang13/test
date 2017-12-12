
function Check($item, $Value){    if ($item.Contains($Value))    {        echo "tracert - Path OK"    }    else {        echo "tracert - Path WRONG"        echo $item    }}
echo "========== MORNING CHECK ================"
echo "Check Path to NHC SS001"$trace = tracert -d 10.184.32.5
$item = $trace.Item(6)Check $item "10.184.33.57" 
$item = $trace.Item(8)Check $item "10.184.32.5" 
echo "======================================="
echo "Check Path to NHC SS002"$trace = tracert -d 10.184.32.6
$item = $trace.Item(6)Check $item "10.184.33.57" 
$item = $trace.Item(8)Check $item "10.184.32.6" 
echo "======================================="
echo "Check Path to SSC SS001"$trace = tracert -d 10.184.0.5
$item = $trace.Item(6)Check $item "10.184.1.57" 
$item = $trace.Item(8)Check $item "10.184.0.5" 
echo "======================================="
echo "Check Path to SSC SS002"$trace = tracert -d 10.184.0.6
$item = $trace.Item(6)Check $item "10.184.1.57" 
$item = $trace.Item(8)Check $item "10.184.0.6" 
echo "======================================="
echo "Check Path to HK"$trace = tracert -d 130.199.33.3
$item = $trace.Item(6)Check $item "10.184.33.57" 
$item = $trace.Item(12)Check $item "10.184.152.4"
$item = $trace.Item(22)Check $item "130.199.33.3" 
pause

