<template>
  <div>
    <div class="columns is-mobile"> 
      <div class="column is-8">
        <h1 class="title has-text-centered">Drivers</h1>
        <div class="columns is-multiline is-mobile is-gapless">
          <div class="column is-half" v-for="driver in drivers" v-bind:key="driver.CarIdx">
            <button v-on:click="driverButtonClicked(driver.CarNumber)" class="button is-fullwidth is-primary is-outlined" :class="carButtonStyling(driver.CarNumber)">#{{ driver.CarNumber }} {{ driver.UserName }}</button>
          </div>
        </div>
      </div>
      <div class="column is-4">
        <h1 class="title has-text-centered">Cameras</h1>
        <div class="columns is-multiline is-mobile is-gapless">
          <div class="column is-half" v-for="cameraGroup in cameraGroups" v-bind:key="cameraGroup.id">
            <button v-on:click="camButtonClicked(cameraGroup.id)" class="button is-fullwidth is-primary is-outlined" :class="camButtonStyling(cameraGroup.id)">{{ cameraGroup.name }}</button>
          </div>
        </div>
      </div>
    </div>
    <div class="container submitButtonContainer">
      <button  
        v-on:click="submitButtonClicked"
        class="button is-fullwidth" 
        :class="submitButtonStyling()"
        :disabled="!this.isConnected"
      >
        {{ submitButtonText() }}
      </button >
    </div>
  </div>
</template>

<script>
export default {
    name: "controls",
    data() {
      return {
        drivers: null,
        selectedDriverNum: 0,
        selectedCameraGroup: 0,
        cameraGroups: cameraGroups,
        isConnected: false,
        driverCheckInterval: null
      }
    },
    methods: {
      carButtonStyling(carNum) {
        return {
          "is-focused": carNum == this.selectedDriverNum 
        }
      },
      camButtonStyling(num) {
        return {
          "is-focused": num == this.selectedCameraGroup
        }
      },
      submitButtonStyling() {
        return {
          "is-success": this.isConnected,
          "is-danger": this.isConnected === false
        }
      },
      submitButtonText() {
        if (this.isConnected) {
          return "Submit"
        } else {
          return "Not Connected"
        }
      },
      camButtonClicked(num) {
        this.selectedCameraGroup = num
        this.$forceUpdate()
      },
      driverButtonClicked(carNum) {
        this.selectedDriverNum = carNum
        this.$forceUpdate()
      },
      submitButtonClicked() {
        if (this.isConnected) {
          console.log(`change camera to ${this.selectedCameraGroup} focusing on car #${this.selectedDriverNum}`)
          changeView(this.selectedDriverNum, this.selectedCameraGroup)
          this.$buefy.toast.open({
            message: 'Camera Changed!',
            type: 'is-success'
          })
        }
      },
      healthcheck() {
        fetch("/ack").then(res => {
            return res.json()
          }
        ).then(ack => {
          if (ack.connected === true && this.isConnected === false) {
            this.isConnected =  true
            getDrivers().then(drivers => {this.drivers = drivers})
            this.driverCheckInterval = setInterval(() => {
              getDrivers().then(drivers => {this.drivers = drivers})
            }, 30000);
          } else if (!ack.connected && this.isConnected) {
            this.isConnected = false
            this.drivers = []
            closeInterval(this.driverCheckInterval)
          }
        })
      }
    },
    created() {
      this.healthcheck()
      setInterval(() => {
        this.healthcheck()
      }, 2000);
    },
}

const cameraGroups = [
  {
    id: 1,
    name: "Nose"
  },
  {
    id: 2,
    name: "Gearbox"
  },
  {
    id: 3,
    name: "Roll Bar"
  },
  {
    id: 4,
    name: "LF Susp"
  },
  {
    id: 5,
    name: "LR Susp"
  },
  {
    id: 6,
    name: "Gyro"
  },
  {
    id: 7,
    name: "RF Susp"
  },
  {
    id: 8,
    name: "RR Susp"
  },
  {
    id: 9,
    name: "Cockpit"
  },
  {
    id: 10,
    name: "Scenic"
  },
  {
    id: 11,
    name: "TV3"
  },
  {
    id: 12,
    name: "TV1"
  },
  {
    id: 14,
    name: "TV Static"
  },
  {
    id: 15,
    name: "TV Mixed"
  },
  {
    id: 16,
    name: "Pit Lane"
  },
  {
    id: 17,
    name: "Pit Lane 2"
  },
  {
    id: 18,
    name: "Blimp"
  },
  {
    id: 19,
    name: "Chopper"
  },
  {
    id: 20,
    name: "Chase"
  },
  {
    id: 21,
    name: "Far Chase"
  },
  {
    id: 22,
    name: "Rear Chase"
  },
]

async function getDrivers() {
  const res = await fetch("/api/session/drivers")
  const data = await res.json()
  return data;
}

function changeView(car_number, camera_group) {
  // Build formData object.
  let formData = new FormData();
  formData.append("driver_number", car_number);
  formData.append("camera_group", camera_group);
  fetch("api/changeview", {
    body: formData,
    method: "post",
  });
}

</script>