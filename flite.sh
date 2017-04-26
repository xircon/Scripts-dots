 #!/usr/bin/env bash
text="$(xsel -o)"
flite -voice ~/Music/cmu_us_rms.flitevox --setf duration_stretch=1.07 -t "$text"
exit 0