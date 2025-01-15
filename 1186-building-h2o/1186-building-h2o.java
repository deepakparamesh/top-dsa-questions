class H2O {

    
        private Semaphore hydrogenSemaphore = new Semaphore(2);

        private Semaphore oxygenSemaphore = new Semaphore(1);
        private CyclicBarrier barrier= new CyclicBarrier(3);

    public H2O() {
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		hydrogenSemaphore.acquire();
        try {
            barrier.await();
            releaseHydrogen.run();
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            hydrogenSemaphore.release();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxygenSemaphore.acquire();
        try{
            barrier.await();
            releaseOxygen.run();
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            oxygenSemaphore.release();
        }
    }
}