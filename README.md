# Uniswap V2 Deployement Tools.

Please clone `uni-v2` and `vvet` repos alongside repo.

## Disclaimer
Redistributions of source code must retain this list of conditions and the following disclaimer.

Neither the name of VeChain (VeChain Foundation) nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

// **Please note this is a draft and this code is under heavy development. NOT to be used in production.**

## How TO

You are encouraged to read the `Makefile` first before execute below commands.

### Install depedencies
```bash
make install
```

### Deploy vVET
```bash
make deploy_vvet network={http://url} \
    private={private_key} \
    vvet={/path/to/vvet.json} 
```

### Deploy Factory + Router 02 of Uni v2
```bash
make deploy_univ2 network={http://url} \
    private={private_key} \
    factory={/path/to/UniswapV2Factory.json} \
    router{/path/to/UniswapV2Router02.json} \
    vvetaddress={0x....}
```

### Create Pool of vVET + VTHO
```bash
make create_pool network={http://url} \
    private={private_key} \
    factory={/path/to/UniswapV2Factory.json} \
    factoryaddress={0x...} \
    vvetaddress={0x...} \
    vthoaddress={0x...}
```

## Testnet

Currently, some contracts are deployed on `testnet`:

| Contract       | Address                                    |
| -------------- | ------------------------------------------ |
| vVET           | 0x535b9a56c2f03a3658fc8787c44087574eb381fd |
| vtho           | 0x0000000000000000000000000000456e65726779 |
| factory        | 0x8d77f31c128c88b52a148167cdc5439cb4bb11db |
| router02       | 0x4c2204ebc042197a728bfe1a771301177d018e32 |
| vVET/VTHO pool | 0x40d1a9b8b27d4f6799513575b957aaf1e0688d8a |
