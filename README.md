# xsdata for BTLx 1.1 files

This is simple test project which tries to validate BTLx files from
[design2machine](https://www.design2machine.com/) against the XSD and use [xsdata]([xsdata](https://pypi.org/project/xsdata/)) to parse them.

As there are no explicit BTLx V1.1 files available, the exisiting V1.0 files
are forcefully upgraded to V1.1, which leads to some errors.

This is the list of validated files:

```
✔️  https://www.design2machine.com/example-btlx/iframetext/lap-joint/ridge-lap.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/lap-joint/ridge-lap2.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/lap-joint/lap-joint.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/lap-joint/slot.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/lap-joint/front-slot.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/simple-scarf/simple-scarf.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/simple-scarf/scarf-joint.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/step-joint/step-joint.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/step-joint/step-joint-notch.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/bird-mouth/bird-mouth.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/bird-mouth/hip-bird-mouth.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/cutting/cut.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/cutting/double-cut.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/cutting/longitudinal-cut.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/cutting/ridge-or-valley-cut.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/cutting/all-cuts.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/log-construction/half-lap.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/log-construction/tyrolean-dovetail.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/log-construction/tyrolean-dovetail-t-connection.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/log-construction/klingschroth.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/log-construction/frosch.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/log-construction/dovetail.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/planing/planing.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/planing/chamfer.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/planing/round-arch.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/tenon-mortise.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/tenon-mortise-front.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/dovetail-tenon-mortise.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/dovetail-mortise-front.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/house.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/tenon/house-mortise.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/contour-outline/free-contour.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/nesting/nesting.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/prefabrication/prefabricated-wall.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/prefabrication/whole-log-wall.btlx  
✔️  https://www.design2machine.com/example-btlx/iframetext/text-marking/marking.btlx
✔️  https://www.design2machine.com/example-btlx/iframetext/text-marking/text-output.btlx       
✔️  https://www.design2machine.com/example-btlx/iframetext/profile-head/profile-front.btlx     
✔️  https://www.design2machine.com/example-btlx/iframetext/profile-head/profile-head-cambered.btlx
❌  https://www.design2machine.com/example-btlx/iframetext/profile-head/profile-head.btlx      
```
