= Notes =

`hello.exe_signed` was created using github actions (CI) and codesigner.

`osslsigncode attach-signature` modifies the PE header by adding the PE checksum.
That is why `hello.exe_signed` is different from `hello.exe_reattached`.
Thanks to `pe_header_to_zero.py` it is possible to reset the PE checksum
back to `0` as it originally is in `hello.exe` and `hello.exe_signed`.

```
osslsigncode verify -in hello.exe_signed
```

```
osslsigncode extract-signature -in hello.exe_signed -out hello.exe_signature
```

```
osslsigncode remove-signature -in hello.exe_signed -out hello.exe_removed
```

```
diff hello.exe hello.exe_removed
```

```
vbindiff hello.exe hello.exe_removed
```

```
diffoscope hello.exe hello.exe_removed
```

```
osslsigncode attach-signature -sigin hello.exe_signature -in hello.exe -out hello.exe_reattached
```

```
cmp hello.exe hello.exe_reattached
```

```
cmp -l hello.exe hello.exe_reattached
```

```
sudo apt install pev
```

```
readpe hello.exe_signed
```

```
./pe_header_to_zero.py
```

```
readpe hello.exe_reattached_pe_header_to_zero
```
